from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from exception import customexception
import sys

def refined_query(query,chat_model):
    try:
        prompt_text_refined=f"Query: {query}\n use the query to form a question which gets embedded to get relevant information and images,so the question must include a key word image. "
        prompt_chat=ChatPromptTemplate.from_template(prompt_text_refined) 
        summarize_chain_refined = {"query": lambda x: query} | prompt_chat | chat_model | StrOutputParser()
        refined__query=summarize_chain_refined.invoke(query) 
        return refined__query
    except Exception as e:
        raise customexception(e,sys)

def final_result(combined_information,query,chat_model):
    try:
        prompt_text_chat=f"Query: {query}\n answer the query by using the combined information only if asked about image don't consider it \n if no details is present in the combined information then reply with 'the book is all about the medical anotomy'\n{combined_information}"
        prompt_chat = ChatPromptTemplate.from_template(prompt_text_chat)
        summarize_chain_chat = {"combined_information": lambda x: combined_information} | prompt_chat | chat_model | StrOutputParser()
        response=summarize_chain_chat.invoke(query)
        return response
    except Exception as e:
        raise customexception(e,sys)
