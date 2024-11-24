from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from exception import customexception
import sys
from dotenv import load_dotenv
load_dotenv()
def load_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return embedding_model
def load_chat_model():
    chat_model=ChatGoogleGenerativeAI(
    model="gemini-pro",temperature=0,max_tokens=2000,
    timeout=2000)
    return chat_model
def load_img_model():
    img_model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",temperature=0,max_tokens=2000,
    timeout=4000)
    return img_model
def load_anthropic_model():
    try:
        a="ANTHROPIC_API_KEY"
        return a
    except Exception as e:
        raise customexception(e,sys)
