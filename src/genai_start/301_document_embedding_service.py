from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
import pickle   
# user defined
from config import set_environment

def embed_documents_and_save(documents, folder_path, file_name):
    """
    Embed the given documents and save the embeddings to a file.
    
    Args:
        documents (list): The list of documents to embed.
        folder_path (str): The path to save the embeddings.
        file_name (str): The name of the file to save the embeddings.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    embedding = embeddings.embed_documents(documents)

    try:
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            pickle.dump(embedding, f)
    finally:
        print(f"Embedding saved to {file_path}")


if __name__ == "__main__":
    """
    Embed documents and save them to a file.
    This is a sample document embedding service.
    It embeds a list of documents and saves the embeddings to a file.
    The embedding is done using the GoogleGenerativeAIEmbeddings class.
    The embedding is saved in a pickle file.
    The file is saved in the data/embeddings/document_embeddings/ folder.
    """
    # Set environment variables
    set_environment()

    # Example documents to embed
    try:
        folder_path = os.getenv("DOCUMENT_EMBEDDING_FOLDER_PATH", "data/embeddings/document_embeddings/")
        file_name = os.getenv("DOCUMENT_EMBEDDING_FILE_NAME", "embed_doc1.pkl")

        documents = ["Hello world", "Goodbye world"]

        # Embed the documents and save them to a file
        embed_documents_and_save(documents, folder_path=folder_path, file_name=file_name)

    finally:
        print(f"Embedding saved to {os.path.join(folder_path, file_name)}")