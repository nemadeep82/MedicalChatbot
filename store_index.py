from src.helper import text_split, load_pdf, ret_huggingface_embeddings_obj
from langchain_pinecone import PineconeVectorStore
#from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

print("PINECONE_API_KEY - ",PINECONE_API_KEY)

# step 1 - Load the PDF data
extracted_data = load_pdf("C:/genaipjts/medicalchatbot/MedicalChatbot/data/")
print("extracted document size -> ",len(extracted_data))

# step 2 - Chunk the loaded dcouments from pdfs
text_chunks = text_split(extracted_data)
print("chunk size ->",len(text_chunks))

# step 3 - Create embedding object
embeddingObj = ret_huggingface_embeddings_obj()

# step 4 - Create vector index
#os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

index_name = "medical-chatbot"

print("vector store creation started for index - ",index_name)

vectorstore_from_texts = PineconeVectorStore.from_texts(
        [t.page_content for t in text_chunks],
        index_name=index_name,
        embedding=embeddingObj
    )

print("vector store creation done")

