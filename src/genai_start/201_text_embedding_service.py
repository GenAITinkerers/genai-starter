### Import libraries
# inbuit
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
import os
import pickle

# user defined
from config import set_environment
# ### Set environment variables
set_environment()

# os.environ['GOOGLE_API_KEY']


# ### Create an instance of the GoogleGenerativeAIEmbeddings class

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# ### use embeddings to embed text and save in file
def embed_text_and_save(text, folder_path, file_name):
    """
    Embed the given text and save the embedding to a file.
    
    Args:
        text (str): The text to embed.
        file_path (str): The path to save the embedding.
    """
    embedding = embeddings.embed_query(text)

    try:
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            pickle.dump(embedding, f)
    finally:
        print(f"Embedding saved to {file_path}")

def main():
    """
    Main function to embed text and save it to a file.
    
    This is a sample text embedding service.
    It embeds a given text and saves the embedding to a file.
    The embedding is done using the GoogleGenerativeAIEmbeddings class.
    The embedding is saved in a pickle file.
    The file is saved in the data/embeddings/text_embeddings/ folder.
    """
    try:
        folder_path = os.getenv("TEXT_EMBEDDING_FOLDER_PATH", "data/embeddings/text_embeddings/")
        file_name = os.getenv("TEXT_EMBEDDING_FILE_NAME", "first_embed2.pkl")

        text = "This is a sample text for embedding."

        # Embed the text and save it to a file
        embed_text_and_save(text, folder_path=folder_path, file_name=file_name)

    finally:
        print(f"Embedding saved to {os.path.join(folder_path, file_name)}")

if __name__ == "__main__":
    main()