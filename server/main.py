from fastapi import FastAPI, Query
from cleaner import Cleaner
from loader import Loader
from trainer import Trainer
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

# @app.get("/get_dicty")
# def get_dicty():
#     return dicty

@app.get("/get_dicty")
def get_dicty():
    loader = Loader()
    cleaner = Cleaner()
    trainer = Trainer()

    df = loader.load()
    cleaned_df = cleaner.cleaner(df)
    trainer.init_dicty_structure(cleaned_df)
    dicty = trainer.calculate_probabilities()
    return dicty

@app.get("/predict")
def predict(
    age: str = Query(...),
    income: str = Query(...),
    student: str = Query(...),
    credit_rating: str = Query(...)
):
    global dicty
    user_dict = {
        "age": age,
        "income": income,
        "student": student,
        "credit_rating": credit_rating
    }

    score_yes = 1.0
    score_no = 1.0


    for feature, value in user_dict.items():
        prob_yes = dicty["yes"][feature].get(value, 1e-6)
        prob_no = dicty["no"][feature].get(value, 1e-6)
        score_yes *= prob_yes
        score_no *= prob_no
    total = score_yes + score_no
    percent_yes = round((score_yes / total) * 100, 2)
    percent_no = round((score_no / total) * 100, 2)

    prediction = "yes" if score_yes > score_no else "no"

    return {
        "percent_yes": f"{percent_yes}%",
        "percent_no": f"{percent_no}%",
        "prediction": prediction
    }


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

