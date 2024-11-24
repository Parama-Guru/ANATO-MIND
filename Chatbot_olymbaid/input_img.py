import os
import base64
from langchain_core.messages import HumanMessage
from Chatbot_olymbaid.model_api import load_img_model
from langchain_core.prompts import ChatPromptTemplate

model_img=load_img_model()
def encode_image(image_path):
    """Getting the base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
def get_image_from_director(path):
    for img_file in sorted(os.listdir(path)):
          if img_file.endswith(".jpg"):
              img_path = os.path.join(path, img_file)
    return img_path

def delete_previous_images(save_dir):
        for filename in os.listdir(save_dir):
            file_path = os.path.join(save_dir, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path) 
                
def img_output():
    path="/Users/guru/ai_ml_olympaid/uploaded_images"
    image_path=get_image_from_director(path)
    img_base64=encode_image(image_path)
    prompt = """You are an assistant tasked with summarizing images for retrieval. \
    These summaries will be embedded and used to retrieve the raw image. \
    Give a concise summary of the image that is well optimized for retrieval."""
    repsonse=image_summarize(img_base64, prompt)
    query=extract_refined_query(repsonse)
    delete_previous_images(path)
    return query


def extract_refined_query(text):
    # Find the start of the refined query
    start_index = text.find("**Question:**") + len("**Question:**")
    
    # Extract the refined query
    refined_query = text[start_index:].strip().strip('"')
    
    return refined_query
def image_summarize(img_base64, query):
    # Construct the prompt
    prompt_text_refined = f"Query: {query}\nUse the query and image to form a question related to the image to fetch data related to the image, which will be embedded to search in the vector database."
    
    # Assuming ChatPromptTemplate is some kind of template system
    prompt = prompt_text_refined.format(query=query) 

    # Create the message content
    message_content = [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}}
    ]

    # Invoke the model
    msg = model_img.invoke([HumanMessage(content=message_content)])

    # Process the response
    response = msg.content

    return response