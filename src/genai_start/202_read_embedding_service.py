import os
import pickle


def read_embedding_from_file(folder_path, file_name):
    """
    Read the embedding from a file.
    
    Args:
        file_path (str): The path to the file containing the embedding.
        
    Returns:
        list: The embedding vector.
    """
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'rb') as f:
        return pickle.load(f)
    


if __name__ == "__main__":
    """
    Read the embedding from a file and print its type and length.
    This is a sample text embedding service.
    It reads the embedding from a file and prints its type and length.
    The embedding is saved in a pickle file.
    The file is saved in the data/embeddings/text_embeddings/ folder.
    """
    try:
        folder_path = os.getenv("TEXT_EMBEDDING_FOLDER_PATH", "data/embeddings/text_embeddings/")
        file_name = os.getenv("TEXT_EMBEDDING_FILE_NAME", "first_embed2.pkl")

        # Read the embedding from the file
        text_embedding = read_embedding_from_file(folder_path=folder_path, file_name=file_name)

        embedding_statistics = {
            "type": type(text_embedding),
            "length": len(text_embedding),
            "first_five_elements": text_embedding[:5] if isinstance(text_embedding, list) else None
        }
        print(embedding_statistics)
    finally:
        print(f"Embedding read from {os.path.join(folder_path, file_name)}")
