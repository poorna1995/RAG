

### Chat Application using Retrieval-Augmented Generation (RAG)

This project explores a **Retrieval-Augmented Generation (RAG)** approach for answering questions based on information extracted from a set of PDF documents. The primary goal is to create an intelligent Question-Answering (QA) tool that provides accurate, contextually relevant responses derived directly from the uploaded documents.

### What is Retrieval-Augmented Generation (RAG)?

RAG combines information retrieval and generation, enhancing response quality by adding relevant external context. It consists of two key components:

1. **Retriever**: Finds relevant text (documents or passages) based on a user query.
2. **Generator**: Uses the retrieved information to create accurate, context-aware responses.


### RAG Workflow
![RAG System Flow](https://github.com/user-attachments/assets/d549a555-af8f-4371-a62f-6ac7733452f9)

<div style="text-align: center;">
    RAG System Flow
</div>


### Why Use RAG in This Project?

The goal of this project is to generate accurate, contextually relevant responses based on document content. RAG is a perfect fit because it enables:

1. **Ensuring Contextual Precision**: RAG retrieves specific document content, grounding responses within relevant text for accurate answers.
2. **Minimizing Errors**: Combines retrieval with generation to reduce irrelevant or fabricated information, enhancing answer reliability.
3. **Adapting Easily to New Data**: Allows seamless updates to the document store without retraining, supporting dynamic datasets.
4. **Providing a Streamlined User Experience**: Delivers precise, real-time answers that align directly with user queries.

Now that we understand what RAG is and the simple workflow involved, let's delve into the technical aspects required to achieve this integration, including text-splitting, vectorization, retrieval mechanisms, and generation.

To simplify the engineering tasks required for building and scaling the project, we utilize the Langchain framework.

![Langchain Framework](https://github.com/user-attachments/assets/32f3bf35-7134-4d42-844c-c49de701c6f7)

<div style="text-align: center;">
    Langchain Framework
</div>

## Implementation Steps

![Rag](https://github.com/user-attachments/assets/482dd56e-c1c6-4609-aebe-b2331eacda5b)

<br><br>

### 1. Clone the Repository

To get started, clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-folder>

### Create a virtual environment:
it is a good practice to use a virtual environment to manage your project dependencies.

 ```bash
 python -m venv venv
 venv\Scripts\activate


### Install Packages: Make sure you have pip installed.

 ```bash
 pip install -r requirements.txt


### Set Up Environment Variables
Create a .env file in the root of your project directory and add the necessary environment variables.

 ```bash
 PINECONE_API_KEY=your_pinecone_api_key
 GROQ_API_KEY=your_groq_api_key


Replace your_pinecone_api_key and your_groq_api_key with your actual API keys.


### Run the Streamlit Application:

 ```bash
 streamlit run app.py









