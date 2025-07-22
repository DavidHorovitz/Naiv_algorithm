import pandas as pd

class Loader:
    def load(self,file):
        df = pd.read_csv(file)
        return df

# a=Loader()
# a.load('../data/buy_computer_data.csv')