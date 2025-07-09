import pandas as pd
from pprint import pprint


df = pd.read_csv('buy_computer_data.csv')
# print(df.head())
# counts= df.groupby('Buy_Computer').size()

# total=df['Buy_Computer'].count()
# print(f"{df.groupby('Buy_Computer').size()}/{df.Buy_Computer.count()}")
dicty = {}
#
# for key in counts.index:
#     value = counts[key]
#     dicty[key] = value/total
# for key , value in dicty.items():
#     print(key,value)


# print(df.iloc[:, 1].value_counts())

# for key in counts.index:
#     value = counts[key]
#     dicty[key] = value/total
# print(df.groupby('Buy_Computer') .iloc[:, 1].value_counts())
# dicti2={df[0]:}


# def total(table :pd):
#     counts = df.groupby('Buy_Computer').size()
#     totaly = df['Buy_Computer'].count()
#
#     for key in counts.index:
#         value = counts[key]
#         dicty[key] = value/total
#
#     print(f"{counts}/{totaly}")

def insert_data():
    global dicty
    dicty ={"yes":{},"no":{}}
    feature_columns = [coloom for coloom in df.columns if coloom not in ['id', 'Buy_Computer']]

    for choice in ["yes", "no"]:
        for coloom in feature_columns:
            # lst = df[value].unique().tolist()
            dicty[choice][coloom]={}
            for val in df[coloom].unique():
                dicty[choice][coloom][val] = None
    #     dicty["yes"]={age:{},income:{},student:{},credit_rating:{}}
    # dicty["no"]={age:{},income:{},student:{},credit_rating:{}}


    return dicty


def insert_How_many():
    global  dicty
    feature_columns = [coloom for coloom in df.columns if coloom not in ['id', 'Buy_Computer']]

    for choice in ['yes','no']:
        condition1 = df[df["Buy_Computer"] == choice]
        total = len(condition1)

        for collom in feature_columns:
            for value in df[collom].unique():
                count = len(condition1[condition1[collom]==value])
                count+=1
                total+=df[collom].nunique()
                result =count / total
                result = round(result,3)
                dicty[choice][collom][value] = result
    return dicty
    # both = condition1[condition1[coloom] == col]
    #
    # sumy1 = len(both)
    # sumy2 = len(condition1)
    #
    # return sumy1 / sumy2

insert_data()
insert_How_many()
pprint(dicty)