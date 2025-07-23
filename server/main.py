from fastapi import FastAPI
from server.cleaner import Cleaner
from server.loader import Loader
from server.trainer import Trainer
import json
import uvicorn


app = FastAPI()

dicty = None

@app.on_event("startup")
async def startup_event():
    global dicty

    loader = Loader()
    df = loader.load()

    cleaner = Cleaner()
    cleaned_df = cleaner.cleaner(df)

    trainer = Trainer()
    trainer.init_dicty_structure(cleaned_df)
    dicty = trainer.calculate_probabilities()

    with open("dicty.json", "w") as f:
        json.dump(dicty,f)

@app.get("/get_dicty")
def get_dicty():
    return dicty


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

