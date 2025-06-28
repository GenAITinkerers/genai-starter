import os
import pickle

def read_document_embedding_from_file(folder_path, file_name):
    """
    Read the document embedding from a file.
    
    Args:
        folder_path (str): The path to the folder containing the embedding file.
        file_name (str): The name of the file containing the embedding.
        
    Returns:
        list: The document embedding vector.
    """
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'rb') as f:
        return pickle.load(f)
    

if __name__ == "__main__":
    """
    Read the document embedding from a file and print its type and length.
    This is a sample document embedding service.
    It reads the embedding from a file and prints its type and length.
    The embedding is saved in a pickle file.
    The file is saved in the data/embeddings/document_embeddings/ folder.
    """
    try:
        folder_path = os.getenv("DOCUMENT_EMBEDDING_FOLDER_PATH", "data/embeddings/document_embeddings/")
        file_name = os.getenv("DOCUMENT_EMBEDDING_FILE_NAME", "embed_doc1.pkl")

        # Read the embedding from the file
        document_embedding = read_document_embedding_from_file(folder_path=folder_path, file_name=file_name)

        embedding_statistics = {
            "type": type(document_embedding),
            "length": len(document_embedding),
            # "first_five_elements": document_embedding[:5] if isinstance(document_embedding, list) else None
        }
        print(embedding_statistics)
    finally:
        print(f"Embedding read from {os.path.join(folder_path, file_name)}")