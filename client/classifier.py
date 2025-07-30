class Check_input():
    def __init__(self,dicty,df):
        self.dicty = dicty
        self.df = df
        self.user_dict={}

    def checker(self, user_dict)-> dict:

        # expected_keys = [col for col in self.df.columns if col not in ['id', 'Buy_Computer']]
        expected_keys = [key for key in self.dicty["yes"].keys()]
        if set(user_dict.keys()) != set(expected_keys):
            print(f" Error: dictionary must have exactly these keys: {expected_keys}")
            return {
                "error": True,
                "message": f"Error: dictionary must have exactly these keys: {expected_keys}"
            }

        self.user_dict = user_dict
        score_yes = 1.0
        score_no = 1.0

        for feature in self.user_dict:
            value = self.user_dict[feature]
            prob_yes = self.dicty["yes"][feature].get(value, 1e-6)
            prob_no = self.dicty["no"][feature].get(value, 1e-6)

            score_yes *= prob_yes
            score_no *= prob_no

        total_yes = len(self.df[self.df["Buy_Computer"] == "yes"])
        total_no = len(self.df[self.df["Buy_Computer"] == "no"])
        total_all = total_yes + total_no

        prior_yes = total_yes / total_all
        prior_no = total_no / total_all

        score_yes *= prior_yes
        score_no *= prior_no

        prediction = "yes" if score_yes > score_no else "no"

        return {
            "error": False,
            "score_yes": round(score_yes, 6),
            "score_no": round(score_no, 6),
            "prediction": prediction
        }
        # print("\nresult:")
        # print(f"score_yes = {round(score_yes,3)}")
        # print(f"score_no = {round(score_no,3)}")
        # if score_yes > score_no:
        #     print("\nyeeeees")
        # else:
        #     print("\nnooooo")


#
# a=Check_input()
#
# result =a.checker({"age":"youth","income":"medium","student":"no","credit_rating":"fair"})
