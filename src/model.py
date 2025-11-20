import numpy as np 
import pandas as pd
from transformers import pipeline 

def get_pipeline(task: str = "text-classification", 
                 model: str = "cardiffnlp/twitter-roberta-base-sentiment-latest"):
    return pipeline(task, model)

def get_label_predictions(pipeline, conversion, sentences = []):
  try: sentences_list = sentences.tolist() 
  except: sentences_list = sentences
  predictions = pipeline(sentences_list)
  predictions = [prediction['label'] for prediction in predictions]
  predictions = conversion(predictions)
  return predictions