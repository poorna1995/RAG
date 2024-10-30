import os
import uuid
import time
import streamlit as st
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import asyncio

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_pinecone.embeddings import PineconeEmbeddings
from langchain.schema import Document  # Import the Document class
# from langchain_community.vectorstores import Pinecone



# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'), environment='us-west1-gcp')  # Adjust environment as needed
index_name = "langchain-rag"  # Specify the index name

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

# Load and preprocess the PDF documents
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return [Document(page_content=page.page_content) for page in loader.load()]  # Convert to Document objects

# process the data - splitting into chunks
def process_text(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
    return text_splitter.split_documents(pages)  # Pass Document objects

# created a vector database using pineonce vector
def create_pinecone_vector_store(processed_texts):
    embedding_model = HuggingFaceEmbeddings()  # Use a suitable model for embeddings
    vector_store = PineconeVectorStore(index=index,embedding = embedding_model)

    ids = [str(uuid.uuid4()) for _ in processed_texts]
    
    # Add documents with embeddings to Pinecone
    vector_store.add_documents(processed_texts, ids=ids)

# create the chat prompt for the response
def chat(query,processed_texts):
    embedding_model = HuggingFaceEmbeddings()
    # Initialize the language model
    llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile", temperature=0)

    prompt_template = ChatPromptTemplate.from_template("""
     Answer the question based only on the following context:
        {context}

        Question: {question}
        """
    )

    # Prepare inputs for the chain
    inputs = {
        "context": processed_texts,  # Use the joined context
        "question": query
    }

    # Create a chain of the prompt and the language model
    rag_chain = (
        prompt_template
        | llm
        | StrOutputParser()
    )

    # Invoke the chain with the prepared inputs
    response = rag_chain.invoke(inputs)
    return response

# Async function to process the PDF in the background
async def process_pdf_background(file_path):
    with ThreadPoolExecutor() as pool:
        pages = await asyncio.get_event_loop().run_in_executor(pool, load_pdf, file_path)
        return await asyncio.get_event_loop().run_in_executor(pool, process_text, pages)


# Main Streamlit app
def main():
    st.title("RAG System")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.text("Processing PDF... This may take a few seconds.")

        # Asynchronously process the PDF
        processed_texts = asyncio.run(process_pdf_background(file_path))

        if processed_texts:
            st.success("PDF Processed Successfully!")
            st.write(f"Extracted {len(processed_texts)} documents.")
            create_pinecone_vector_store(processed_texts)
            st.success("Vector Store Created Successfully!")

            query = st.text_input("Ask a question about NCERT topics:")
            
            if query:
                response = chat(query,processed_texts)  # Pass processed texts as context
                st.write("Response:")
                st.write(response)

if __name__ == "__main__":
    main()