from bson.objectid import ObjectId
from exception import customexception
import sys

def result_mongo(result,collection):
    try:
        mylist=[]
        image_64=[]
        for i in  range(len(result["matches"])):
            value=result["matches"][i]['id']
            mylist.append(collection.find_one({"_id": ObjectId(value)}))
        combined_information = ""
        for i in range(len(mylist)):
          if(mylist[i]["type"]=="text"):
            summary=mylist[i]["summary"]
            context=mylist[i]["context"]
            combined_information += f"context:{context}, summary: {summary}\n"
          elif(mylist[i]["type"]=="image"):
            summary=mylist[i]["summary"]
            combined_information += f"summary: {summary}\n"
            image_64.append(mylist[i]["image_64"])
        return combined_information,image_64
    except Exception as e:
        raise customexception(e,sys)
