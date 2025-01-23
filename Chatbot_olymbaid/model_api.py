from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from exception import customexception
import sys
from dotenv import load_dotenv
load_dotenv()
def load_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    print("loaded embedding model")
    return embedding_model
def load_chat_model():
    chat_model=ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",temperature=0,max_output_tokens=2000,
    timeout=2000)
    print("loaded chat model")
    return chat_model
def load_img_model():
    img_model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",temperature=0,max_output_tokens=2000,
    timeout=4000)
    print("loaded image model")
    return img_model