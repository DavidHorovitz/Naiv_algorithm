import pandas as pd
from pprint import pprint


df = pd.read_csv('buy_computer_data.csv')

dicty = {}

def insert_data():
    global dicty
    dicty ={"yes":{},"no":{}}
    feature_columns = [col for col in df.columns if col not in ['id', 'Buy_Computer']]

    for choice in ["yes", "no"]:
        for coloom in feature_columns:
            dicty[choice][coloom]={}
            for val in df[coloom].unique():
                dicty[choice][coloom][val] = None
    return dicty

def insert_How_many():
    global  dicty
    feature_columns = [col for col in df.columns if col not in ['id', 'Buy_Computer']]

    for choice in ['yes','no']:
        condition1 = df[df["Buy_Computer"] == choice]
        total = len(condition1)

        for column in feature_columns:
            unique_vals = df[column].unique()
            num_unique = len(unique_vals)

            for value in unique_vals:
                count = len(condition1[condition1[column] == value]) + 1  # Laplace
                total_smoothed = total + num_unique  # Laplace
                result = count / total_smoothed
                result = round(result, 3)
                dicty[choice][column][value] = result

            # for value in df[collom].unique():
            #     count = len(condition1[condition1[collom]==value])
            #     count+=1
            #     total+=df[collom].nunique()
            #     result =count / total
            #     result = round(result,3)
            #     dicty[choice][collom][value] = result
    return dicty


insert_data()
insert_How_many()
pprint(dicty)