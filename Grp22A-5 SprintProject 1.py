# Employee Claims Processing System (work trips) at the NL Chocolate Company

# Written by: Group 22A-5, Makenzie Roberts, Neil Stratton, and David Turner
# Date written: Feb 26, 2022
# Project ID: Midterm Sprint Week. Project 1: NL Chocolate Company, Claims Processing System

# Libraries imported

import matplotlib.pyplot as plt
import datetime

# Constants


# All the functions that can be called from main or are utilized by other functions


print()


def Display_Menu():
    print("NL Chocolate Company Claims Processing System")
    print("-"*46)
    print("Enter an Employee Travel Claim - Press 1")
    print("Fun Interview Question  - Press 2")
    print("Cool Stuff with Strings and Dates - Press 3")
    print("Graph Monthly Claim Totals - Press 4")
    print("Quit the Program - Press 5")
    print()


def Emp_Trav_Claim():
    pass


def Fun_Question():
    pass


def Strings_Dates():
    pass


def Graph_Monthly_Totals():
    pass


# Programs main that calls all functions as the user chooses what they want

Display_Menu()
#List = [] # delete if not needed/used

while True:
    Choice = input("Enter choice: (1-5): ")
    if Choice == "1":
        Emp_Trav_Claim()
    elif Choice == "2":
        Fun_Question()
    elif Choice == "3":
        Strings_Dates()
    elif Choice == "4":
        Graph_Monthly_Totals()
    elif Choice == "5":
        print()
        print("Thank you for utilizing the \"Claims Processing System\", have a wonderful day.")
        break
    else:
        print("Not a valid choice - please re-enter")


