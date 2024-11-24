from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pinecone import Pinecone
import os
from dotenv import load_dotenv
from exception import customexception
import sys
load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
def connect_mongodb():
    try:
        uri = "mongodb+srv://paramaguruvh:Guru1910@cluster0.m5ten.mongodb.net/database?retryWrites=true&w=majority&appName=Cluster0"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        db=client["olymbaid_AI_ML"]
        collection=db["data"]
        return collection
    except Exception as e:
        raise customexception(e,sys)

def connect_pineconedb():
    try:
        pc = Pinecone(api_key=PINECONE_API_KEY)
        index = pc.Index("mongo-ai-ml")
        print("true for index")
        return index
    except Exception as e:
        raise customexception(e,sys)


 
