# from loader import Loader as lo
# import pandas as pd
class Cleaner:
    def cleaner(self,df):
        cleaned_df = df.dropna()
        cleaned_df=cleaned_df.drop_duplicates()
        return cleaned_df

# cleaned=Cleaner()
# cleaned.cleaner(lo.load())
