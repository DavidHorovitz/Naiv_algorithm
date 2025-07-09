import pandas as pd


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

def insert_data(age,income,student,credit_rating):
    global dicty
    dicty["yes"]={age:{},income:{},student:{},credit_rating:{}}
    dicty["no"]={age:{},income:{},student:{},credit_rating:{}}
    return dicty


def insert_How_many(coloom):
    global  dicty

    for choice in ['yes','no']:
        condition1 = df[df["Buy_Computer"] == choice]
        total = len(condition1)

        for value in df[coloom].unique():
            both = condition1[condition1[coloom] == value]
            count = len(both)
            result = count / total
            dicty["yes"][coloom][value] = result
    return dicty
    # both = condition1[condition1[coloom] == col]
    #
    # sumy1 = len(both)
    # sumy2 = len(condition1)
    #
    # return sumy1 / sumy2

insert_data("senior","low","yes","fair")
insert_How_many("age")