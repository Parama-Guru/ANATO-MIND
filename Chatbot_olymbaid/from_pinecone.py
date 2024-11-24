from exception import customexception
import sys
def result_pinecone(query,embedding_model,index):
  try:
    embedding=embedding_model.embed_query(query)
    #embedding=embedding.tolist()

    result=index.query(
      vector=embedding,
      top_k=3,
    )
    return result
  except Exception as e:
        raise customexception(e,sys)



