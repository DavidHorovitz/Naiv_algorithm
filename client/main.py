from wsgiref.validate import validator
import time
import uvicorn
from classifier import Check_input
import requests
from fastapi import FastAPI, Query

app = FastAPI()
# response = requests.get("http://dicty_container:8000/get_dicty")  # שם הקונטיינר הראשון ברשת דוקר
# dicty = response.json()
def wait_for_dicty(url, timeout=30):
    for i in range(timeout):
        try:
            print(f"Trying to connect to {url}... Attempt {i+1}")
            response = requests.get(url)
            if response.status_code == 200:
                print("Connected!")
                return response.json()
        except:
            pass
        time.sleep(1)
    raise RuntimeError("Could not connect to dicty server")

dicty = wait_for_dicty("http://dicty_container:8000/get_dicty")




@app.get("/predict")
async def predict(
    age: str = Query(...),
    income: str = Query(...),
    student: str = Query(...),
    credit_rating: str = Query(...)
):
    # dicty = co.dicty
    user_dict = {
        "age": age,
        "income": income,
        "student": student,
        "credit_rating": credit_rating
    }
    answer=Check_input(user_dict,dicty)
    return answer.checker(user_dict)

    # score_yes = 1.0
    # score_no = 1.0
    #
    # for feature in user_dict:
    #     val = user_dict[feature]
    #     prob_yes = dicty["yes"][feature].get(val, 1e-6)
    #     prob_no = dicty["no"][feature].get(val, 1e-6)
    #     score_yes *= prob_yes
    #     score_no *= prob_no
    #
    # total_yes = len(df[df["Buy_Computer"] == "yes"])
    # total_no = len(df[df["Buy_Computer"] == "no"])
    # total = total_yes + total_no
    # prior_yes = total_yes / total
    # prior_no = total_no / total
    #
    #
    # score_yes *= prior_yes
    # score_no *= prior_no
    #
    # total_score=score_no+score_yes
    # percent_yes = (score_yes / total_score) * 100
    # percent_no = (score_no / total_score) * 100
    #
    # prediction = "yes" if score_yes > score_no else "no"
    #
    # return {
    #     "prediction": prediction,
    #     "score_yes": score_yes,
    #     "score_no": score_no,
    #     "percent_yes": round(percent_yes, 2),
    #     "percent_no": round(percent_no, 2)
    # }

# @app.get("/condition")
# async def condition(
#     feature: str = Query(...),
#     value: str = Query(...)
#
# ):
#     # dicty = co.dicty
#
#     if feature not in dicty["yes"]:
#         return {"error": "Invalid feature name"}
#
#     prob_yes = dicty["yes"][feature].get(value, 0.0)
#     prob_no = dicty["no"][feature].get(value, 0.0)
#
#     result = "yes" if prob_yes > prob_no else "no"
#
#     return {
#         "feature": feature,
#         "value": value,
#         "result": result,
#         "P(value | yes)": round(prob_yes, 3),
#         "P(value | no)": round(prob_no, 3)
#     }

# @main (/predictor)


    # validator = Validator(dicty, df)
    # validator.test()

if __name__=="__main__":

    uvicorn.run(app,host="0.0.0.0",port=8000)

    # import uvicorn
    # from fastapi import FastAPI, Query
    # from app.loader import Loader
    # from app.cleaner import Cleaner
    # from app.trainer import Trainer
    # from app.validator import Validator
    # from app.classifier import Check_input
    #
    # app = FastAPI()
    #
    # dicty = None
    # df = None
    #
    #
    # @app.on_event("startup")
    # async def startup_event():
    #     global dicty, df
    #     loader = Loader()
    #     df = loader.load('path/to/your/buy_computer_data.csv')  # עדכן את הנתיב כאן
    #
    #     cleaner = Cleaner()
    #     cleaned_df = cleaner.cleaner(df)
    #
    #     trainer = Trainer()
    #     trainer.insert_data(cleaned_df)
    #     trainer.insert_How_many()
    #     dicty = trainer.dicty
    #
    #
    # @app.get("/predict")
    # async def predict(
    #         age: str = Query(...),
    #         income: str = Query(...),
    #         student: str = Query(...),
    #         credit_rating: str = Query(...)
    # ):
    #     global dicty, df
    #     user_dict = {
    #         "age": age,
    #         "income": income,
    #         "student": student,
    #         "credit_rating": credit_rating
    #     }
    #
    #     score_yes = 1.0
    #     score_no = 1.0
    #
    #     for feature in user_dict:
    #         prob_yes = dicty["yes"][feature].get(user_dict[feature], 1e-6)
    #         prob_no = dicty["no"][feature].get(user_dict[feature], 1e-6)
    #         score_yes *= prob_yes
    #         score_no *= prob_no
    #
    #     total_yes = len(df[df["Buy_Computer"] == "yes"])
    #     total_no = len(df[df["Buy_Computer"] == "no"])
    #     total = total_yes + total_no
    #     prior_yes = total_yes / total
    #     prior_no = total_no / total
    #
    #     score_yes *= prior_yes
    #     score_no *= prior_no
    #
    #     total_score = score_yes + score_no
    #     percent_yes = (score_yes / total_score) * 100
    #     percent_no = (score_no / total_score) * 100
    #
    #     prediction = "yes" if score_yes > score_no else "no"
    #
    #     return {
    #         "prediction": prediction,
    #         "score_yes": round(score_yes, 6),
    #         "score_no": round(score_no, 6),
    #         "percent_yes": round(percent_yes, 2),
    #         "percent_no": round(percent_no, 2)
    #     }
    #
    #
    # @app.get("/condition")
    # async def condition(
    #         feature: str = Query(...),
    #         value: str = Query(...)
    # ):
    #     global dicty
    #
    #     if feature not in dicty["yes"]:
    #         return {"error": "Invalid feature name"}
    #
    #     prob_yes = dicty["yes"][feature].get(value, 0.0)
    #     prob_no = dicty["no"][feature].get(value, 0.0)
    #
    #     result = "yes" if prob_yes > prob_no else "no"
    #
    #     return {
    #         "feature": feature,
    #         "value": value,
    #         "result": result,
    #         "P(value | yes)": round(prob_yes, 6),
    #         "P(value | no)": round(prob_no, 6)
    #     }
    #
    #
    # @app.get("/classify")
    # async def classify(
    #         age: str = Query(...),
    #         income: str = Query(...),
    #         student: str = Query(...),
    #         credit_rating: str = Query(...)
    # ):
    #     global dicty, df
    #     checker = Check_input(dicty, df)
    #     user_input = {
    #         "age": age,
    #         "income": income,
    #         "student": student,
    #         "credit_rating": credit_rating
    #     }
    #     result = checker.checker(user_input)
    #     return result
    #
    #
    # @app.get("/validate")
    # async def validate():
    #     global dicty, df
    #     validator = Validator(dicty, df)
    #     validator.test()
    #     return {"message": "Validation complete - check console/logs for results"}
    #
    #
    # if __name__ == "__main__":
    #     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

