import pandas as pd

class Loader:
    def load(self):
        df = pd.read_csv("data/buy_computer_data.csv")
        return df

# a=Loader()
# a.load('../data/buy_computer_data.csv')