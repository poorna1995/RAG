
# Main Streamlit app
def main():
    st.title("RAG System for NCERT Text")
    
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