


### Let's build a Chat Application using the RAG System

This project explores a **Retrieval-Augmented Generation (RAG)** for answering questions based on information extracted from a set of PDF documents. The primary goal is to create an intelligent Question-Answering (QA) tool that provides accurate, contextually-relevant responses derived directly from the uploaded documents.. 


### What is Retrieval-Augmented Generation (RAG)?

RAG combines information retrieval and generation, enhancing response quality by adding relevant external context. It has two key components:

1. **Retriever**: Finds relevant text (documents or passages) based on a user query.
2. **Generator**: Uses the retrieved information to create accurate, context-aware responses.
 <br><br>


![Rag_general](https://github.com/user-attachments/assets/d549a555-af8f-4371-a62f-6ac7733452f9)


```html
<div style="text-align: center;">
RAG System Flow
</div>


### Rag flow


### Why Rag used in this project:
The goal of this project is to generate accurate, contextually relevant responses based on document content. RAG is a perfect fit because it enables:

1. **Ensuring Contextual Precision**: RAG retrieves specific document content, grounding responses within relevant text for accurate answers.
2. **Minimizing Errors**: Combines retrieval with generation to reduce irrelevant or fabricated information, enhancing answer reliability.
3. **Adapting Easily to New Data**: Allows seamless updates to the document store without retraining, supporting dynamic datasets.
4. **Providing a Streamlined User Experience**: it provides precise, real-time answers that align directly with user queries.

Now, we understand what RAG is and the simple workflow of its. let's start understanding what the technicalities included to achieve such a mixture of the engineering tasks involved like (text-splitting, vectorisation, retrieval mechanism, and generation).

To make this whole process easier and more seamless, we utilize the Langchain framework, which simplifies the engineering tasks required for building and scaling the project.

![langchain](https://github.com/user-attachments/assets/32f3bf35-7134-4d42-844c-c49de701c6f7)
<div style="text-align: center;">
Langchain Frameword
</div>


![image](https://github.com/user-attachments/assets/77f7190c-c9b6-4417-b87c-6aff3d54b3b3)




![Rag](https://github.com/user-attachments/assets/482dd56e-c1c6-4609-aebe-b2331eacda5b)





