import coach as co

class Check_input():
    def __init__(self):
        self.dicty = co.dicty
        self.user_dict={}

    def checker(self,user_input):
        four_parans= [col for col in co.df.columns if col not in ['id', 'Buy_Computer']]
        inp=user_input.strip().split(" ")

        # if len(inp) != 4:
        #     print("4 parameters! (age, income, student, credit_rating)")
        #     return

        for i in range (len(four_parans)):
            self.user_dict[four_parans[i]]=inp[i]

        score_yes = 1.0
        score_no = 1.0

        for feature in self.user_dict:
            value = self.user_dict[feature]
            prob_yes = self.dicty["yes"][feature].get(value, 1e-6)
            prob_no = self.dicty["no"][feature].get(value, 1e-6)

            score_yes *= prob_yes
            score_no *= prob_no

        total_yes = len(co.df[co.df["Buy_Computer"] == "yes"])
        total_no = len(co.df[co.df["Buy_Computer"] == "no"])
        total_all = total_yes + total_no

        prior_yes = total_yes / total_all
        prior_no = total_no / total_all

        score_yes *= prior_yes
        score_no *= prior_no

        print("\nresult:")
        print(f"score_yes = {round(score_yes,3)}")
        print(f"score_no = {round(score_no,3)}")
        if score_yes > score_no:
            print("\nyeeeees")
        else:
            print("\nnooooo")



a=Check_input()
a.checker("youth medium no fair")