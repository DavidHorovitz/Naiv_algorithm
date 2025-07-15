import uvicorn
# from fastapi import FastAPI
#
# app=FastAPI()
#
# @app.get("/")
# async def root():
#     return {"message":"Hello World"}
# @app.get("/red")
# async def red():
#     return {"message" :"Hello red World"}
#
# @app.get("/{name}")
# async def name(name):
#     return {"message :Hello red World1":name}
#
# @app.get("/{age}")
# async def age(age):
#     return {"message :Hello red World2":name}
#
# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8000)

import coach as co
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/predict")
async def predict(
    age: str = Query(...),
    income: str = Query(...),
    student: str = Query(...),
    credit_rating: str = Query(...)
):
    dicty = co.dicty
    user_dict = {
        "age": age,
        "income": income,
        "student": student,
        "credit_rating": credit_rating
    }

    score_yes = 1.0
    score_no = 1.0

    for feature in user_dict:
        val = user_dict[feature]
        prob_yes = dicty["yes"][feature].get(val, 1e-6)
        prob_no = dicty["no"][feature].get(val, 1e-6)
        score_yes *= prob_yes
        score_no *= prob_no

    total_yes = len(co.df[co.df["Buy_Computer"] == "yes"])
    total_no = len(co.df[co.df["Buy_Computer"] == "no"])
    total = total_yes + total_no
    prior_yes = total_yes / total
    prior_no = total_no / total

    # מכפיל לפי חוק בייס
    score_yes *= prior_yes
    score_no *= prior_no

    total_score=score_no+score_yes
    percent_yes = (score_yes / total_score) * 100
    percent_no = (score_no / total_score) * 100

    prediction = "yes" if score_yes > score_no else "no"

    return {
        "prediction": prediction,
        "score_yes": round(score_yes, 3),
        "score_no": round(score_no, 3),
        "percent_yes": round(percent_yes, 2),
        "percent_no": round(percent_no, 2)
    }





@app.get("/condition")
async def condition(
    feature: str = Query(...),
    value: str = Query(...)

):
    dicty = co.dicty

    if feature not in dicty["yes"]:
        return {"error": "Invalid feature name"}

    prob_yes = dicty["yes"][feature].get(value, 0.0)
    prob_no = dicty["no"][feature].get(value, 0.0)

    result = "yes" if prob_yes > prob_no else "no"

    return {
        "feature": feature,
        "value": value,
        "result": result,
        "P(value | yes)": round(prob_yes, 3),
        "P(value | no)": round(prob_no, 3)
    }

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
