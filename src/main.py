import os, csv
import numpy as np
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
# important specify src.model for the tests
from src.model import get_pipeline, get_label_predictions 

app = FastAPI()

class Reviews(BaseModel):
    sentences: list[str]

pipe = get_pipeline() # instantiation just one time
label_to_int = {'negative': 0, 'neutral': 1, 'positive': 2}
int_to_label = {i:l for l,i in label_to_int.items()}
conversion = np.vectorize(label_to_int.get)

if not os.path.exists('data'):
    os.makedirs('data')

CSV_PATH = 'data/sentiment.csv'

if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, mode = 'w', newline = '') as file: # writing mode
        writer = csv.writer(file)
        writer.writerow(["sentence", "sentiment"])

@app.get("/")
async def root(): 
    return {"message": "Welcome to the Machine Innovators Main Page."}

@app.post("/inference")
async def get_predictions(new_sentences: Reviews): 
    predictions = get_label_predictions(pipe, conversion, new_sentences.sentences)
    with open(CSV_PATH, mode = 'a', newline = '') as file: # append mode
        writer = csv.writer(file)
        for sentence, sentiment in zip(new_sentences.sentences, predictions):
            writer.writerow([sentence, int_to_label[int(sentiment)]])
    return {"predictions": predictions.tolist()}

@app.get("/obtain_csv")
async def obtain_csv():
    if os.path.exists(CSV_PATH):
        return FileResponse(CSV_PATH, media_type='text/csv', filename="sentiment.csv")
    else:
        return {"error": "CSV file does not exist. Make some inferences first."}
if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app,
                host = "0.0.0.0", 
                port = 8000) 