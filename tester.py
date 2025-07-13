from pprint import pprint
import coach as co
import pandas as pd


class Tester:
    def __init__(self):
        self.big_table = None
        self.small_table = None
        self.dicty = {}

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

    def list(self):
        lst=[]
        for _,row in self.small_table.iterrows():
            lst.append(row.iloc[-1])
        return lst


    def test(self,big_table,small_table):
        sumy=1
        for row in small_table.iterrows():
            print(row)
            # for param in row:
            #     sumy*=param
            # sumy*=



tester=Tester()
# coach.transfer()
# print(coach.list())
tester.test()




