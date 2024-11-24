from Chatbot_olymbaid.model_api import load_embedding_model
from Chatbot_olymbaid.db_connect import connect_pineconedb
from Chatbot_olymbaid.db_connect import connect_mongodb
from Chatbot_olymbaid.model_api import load_chat_model

def elements ():
    embedding_model=load_embedding_model()
    index=connect_pineconedb()
    collection = connect_mongodb()
    chat_model=load_chat_model()
    return embedding_model,index,collection,chat_model

