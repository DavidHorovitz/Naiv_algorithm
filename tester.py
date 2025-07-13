from pprint import pprint
import coach as co
import pandas as pd

from coach import dicty


class Tester:
    def __init__(self):
        self.big_table = None
        self.small_table = None
        self.dicty = co.dicty

    def transfer(self):
        small_rows = []
        big_rows = []

        for index,row, in co.df.iterrows():
            if index%3==0:
                small_rows.append(row)
            else:
                big_rows.append(row)

        self.small_table=pd.DataFrame(small_rows)
        self.big_table = pd.DataFrame(big_rows)

    # def list(self):
    #     lst=[]
    #     for _,row in self.small_table.iterrows():
    #         lst.append(row.iloc[-1])
    #     return lst

    def predict(self, row):
        score_yes = 1.0
        score_no = 1.0
        for feature in self.dicty["yes"]:
            val = row[feature]
            prob_yes = self.dicty["yes"][feature].get(val, 1e-6)
            prob_no = self.dicty["no"][feature].get(val, 1e-6)
            score_yes *= prob_yes
            score_no *= prob_no

        prior_yes = len(self.big_table[self.big_table["Buy_Computer"] == "yes"]) / len(self.big_table)
        prior_no = len(self.big_table[self.big_table["Buy_Computer"] == "no"]) / len(self.big_table)

        score_yes *= prior_yes
        score_no *= prior_no
        # maximum = max(score_no, score_yes)
        # return maximum
        return "yes" if score_yes > score_no else "no"


    def test(self):

        self.transfer()


        predictions = []
        actual = []

        for _, row in self.small_table.iterrows():
            pred = self.predict(row)
            predictions.append(pred)
            actual.append(row["Buy_Computer"])

        correct = 0
        for i in range(len(predictions)):
            if predictions[i] == actual[i]:
                correct += 1

        total = len(actual)
        accuracy = correct / total

        print("result")
        for i in range(len(predictions)):
            print(f"line {i + 1}: gusse = {predictions[i]}, true = {actual[i]}")

        print(f"\n {accuracy}% ({correct} from {total})")
        # sumy=1
        # for row in small_table.iterrows():
        #     print(row)
            # for param in row:
            #     sumy*=param
            # sumy*=



tester=Tester()
# coach.transfer()
# print(coach.list())

tester.test()




