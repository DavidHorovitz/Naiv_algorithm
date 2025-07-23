# import pandas as pd
# from pprint import pprint
# from cleaner import Cleaner as cl

class Trainer():
    def __init__(self):
        self.dicty = {"yes": {}, "no": {}}
        self.df = None


#
# dicty = {}

    def init_dicty_structure(self, clined_df):
        self.df = clined_df
        feature_columns = [col for col in self.df.columns if col not in ['id', 'Buy_Computer']]
        for choice in ["yes", "no"]:
            for column in feature_columns:
                self.dicty[choice][column] = {}
                for val in self.df[column].unique():
                    self.dicty[choice][column][val] = None
        return self.dicty

    def calculate_probabilities(self):
        if self.df is None:
            raise ValueError("No DataFrame provided. Call insert_data(df) first.")

        feature_columns = [col for col in self.df.columns if col not in ['id', 'Buy_Computer']]

        for choice in ['yes','no']:
            condition_df = self.df[self.df["Buy_Computer"] == choice]
            total = len(condition_df)

            for column in feature_columns:
                unique_vals = self.df[column].unique()
                num_unique = len(unique_vals)

                for value in unique_vals:
                    count = len(condition_df[condition_df[column] == value]) + 1  # Laplace
                    total_smoothed = total + num_unique  # Laplace
                    result = count / total_smoothed
                    result = round(result, 3)
                    self.dicty[choice][column][value] = result

                # for value in df[collom].unique():
                #     count = len(condition1[condition1[collom]==value])
                #     count+=1
                #     total+=df[collom].nunique()
                #     result =count / total
                #     result = round(result,3)
                #     dicty[choice][collom][value] = result
        return self.dicty

# df = pd.read_csv('../data/buy_computer_data.csv')
# trainer = Trainer()
# trainer.insert_data(df)
# dicty = trainer.insert_How_many()
# pprint(dicty)

# insert_How_many()
# pprint(dicty)