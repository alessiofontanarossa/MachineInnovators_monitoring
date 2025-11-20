import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from model import get_pipeline, get_label_predictions

app = FastAPI()

class Reviews(BaseModel):
    sentences: list[str]

pipe = get_pipeline() # instantiation just one time
label_to_int = {'negative': 0, 'neutral': 1, 'positive': 2}
conversion = np.vectorize(label_to_int.get)

@app.get("/")
async def root(): 
    return {"message": "Machine Innovators Main Page"}

@app.post("/inference")
async def get_predictions(new_sentences: Reviews): 
    predictions = get_label_predictions(pipe, conversion, new_sentences.sentences)
    return {"predictions": predictions.tolist()}

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app,
                host = "0.0.0.0", 
                port = 8000) 