from app import trainer as co, classifier as ch
from pprint import pprint


class Menu():
    # def __init__(self):

    def show_menu(self):

        while True:
            user_choice = input("wich of the options do you want?\n1. show the dictionary\n2. check a input\n3. shoe again ")

            match user_choice:
                case "1":
                    pprint(co.dicty)
                case "2":
                    user_params=input("enter the params")
                    checker_obj = ch.Check_input()
                    checker_obj.checker(user_params)
                case "3":
                    continue
                case _:
                    break


manager=Menu()
manager.show_menu()