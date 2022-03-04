# Employee Claims Processing System (work trips) at the NL Chocolate Company

# Written by: David Turner
# Date written: Feb 25, 2022
# Project ID: Midterm Sprint Week. Project 1: NL Chocolate Company, Claims Processing System

# Libraries imported
import datetime

def Display_Menu():
    print()
    print("NL Chocolate Company Claims Processing System")
    print("-"*46)
    print("Enter an Employee Travel Claim - Press 1")
    print("Fun Interview Question  - Press 2")
    print("Cool Stuff with Strings and Dates - Press 3")
    print("Graph Monthly Claim Totals - Press 4")
    print("Quit the Program - Press 5")
    print()

def Dollar_Format(num):


    formatStr = "${:,.2f}".format(num)

    return formatStr

def Difference_Between_Dates(EnDate, StDate):

    # Written By: David Turner
    # Date Written: Feb 25, 2022

    # Description:
    # This function calculates the difference between 2 dates returning value as number of days ex: 7.

    # Parameters:
    # Two dates are sent to this function as arguments,
    # that will be used to calculate to a numerical value.

    # Returns:
    # Returns the numerical value as an integer.
    # Ex: The arguments (2022, 12, 22, 0, 0) and (2022, 12, 15, 0, 0) returned as the int 7,
    # .Days takes your two date inputs after they're subtracted them converts that to days stripping out time

    Dif_Days = (EnDate - StDate).days

    return Dif_Days


def Emp_Trav_Claim():


    # Written By: David Turner
    # Date Written: Feb 25, 2022

    # Description:
    # This function allows an employee to enter as many travel claims as needed.

    # Parameters:
    # Does not require a parameter and does not accept any arguments.
    # Based on user inputs within this function

    # Returns:
    # There is no return with this function as the output is
    # presented prior to returning to main


    # Constants
    DAILY_RATE = 85.00
    RENTAL_CAR_RATE = 65.00
    PER_KM_RATE = 0.17
    BONUS_KM_RATE = 0.04
    EXECUTIVE_RATE = 45.00
    BONUS_DAYS_AMOUNT = 100.00
    DEC_BONUS_RATE = 50.00
    HST = 0.15

    while True:
        # Welcome message
        print()
        print("       ------------------------------------")
        print("         Option 1: Employee Travel Claim")
        print("       ------------------------------------")
        while True:
            # input and validation of the employee number
            Emp_Num = input("Please enter in your 5 digit employee numer (12345): ")
            if Emp_Num == "":
                print("Your employee number cannot be blank - please re-enter.")
            elif len(Emp_Num) != 5:
                print("Your employee number must be 5 digits - please re-enter.")
            elif Emp_Num.isdigit() == False:
                print("Your employee number must contain numbers only - please re-enter.")
            else:
                break

        # Input and validation of the employee's first name
        while True:
            Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890-'")
            First_Name = input("Enter the your first name (type End to exit):        ").title()
            if First_Name == "End":
                exit(User_Choices())
                print()
            elif First_Name == "":
                print("First name must not be blank - please re-enter.")
            elif set(First_Name).issubset(Allowed_Char) == False:
                print("First name contains invalid characters - please re-enter")
            else:
                break

        # Input and validation of the employee's last name
        while True:
            Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890-'")
            Last_Name = input("Enter the your last name:                            ").title()
            if Last_Name == "":
                print("Last name must not be blank - please re-enter.")
            elif set(Last_Name).issubset(Allowed_Char) == False:
                print("Last name contains invalid characters - please re-enter")
            else:
                break

        # Input and validation for the employee trip location
        while True:
            Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'")
            Location = input("Enter the trip location:                             ").title()
            if Location == "":
                print("Trip location can't be blank - please re-enter")
            elif set(Location).issubset(Allowed_Char) == False:
                print("Trip location cannot contain invalid characters - please re-enter")
            else:
                break

        # Input and validation for the employee start and end date
        while True:
            try:
                Start_Date = input("Enter the start date of the claim (YYYY-MM-DD):      ")
                Start_Date = datetime.datetime.strptime(Start_Date, "%Y-%m-%d")
            except:
                print("Start date not a valid format - please re-enter.")
            else:
                break

        while True:
            try:
                End_Date = input("Enter the end date of the claim (YYYY-MM-DD):        ")
                End_Date = datetime.datetime.strptime(End_Date, "%Y-%m-%d")
            except:
                print("End date not a valid format - please re-enter.")
            else:

                if End_Date <= Start_Date:
                    print("End date must be after the start date - please re-enter.")
                else:
                    # Calculate the number of days of the claim and ensure number of days doesn't exceed 7,
                    Num_Days = Difference_Between_Dates(End_Date, Start_Date)  # sends 2 arguments, returns the calced value

                    if Num_Days > 7:
                        print("The number of days exceeds 7 - please re-enter")
                    else:
                        break

        # Input and validation of vehicle used
        while True:
            Allowed_Char = set("RO")
            Vehicle_Type = input("Enter the vehicle used, own or rental (O or R):      ").upper()
            if Vehicle_Type == "":
                print("Vehicle type can't be blank - please re-enter")
            elif set(Vehicle_Type).issubset(Allowed_Char) == False:
                print("Vehilcle type cannot contain invalid characters - please re-enter")
            else:
                break

        # Calculations for the vehicle allowance, rental or own vehicle, and trip distance
        Vehicle_Payout = 0
        Msg = ""
        Kms_Travel = 0
        Kms_TravelDsp = 0
        Kms_Msg = ""
        Vehicle_Type_Selected = ""

        if Vehicle_Type == "R":
            Vehicle_Type_Selected = "Rental"
            Vehicle_Payout = Num_Days * RENTAL_CAR_RATE
            Msg = "Rental Amount:"
            Kms_Msg = ""
            Kms_TravelDsp = ""
        elif Vehicle_Type == "O":
            Vehicle_Type_Selected = "Personal"
            while True:
                try:
                    Kms_Travel = float(input("How many kms were traveled on the work trip?:        "))
                except:
                    print("Kms traveled is not a valid number - please re-enter.")
                if Kms_Travel > 2000:
                    print("Kms travelled for work must be under 2000 kms - please re-enter")
                elif Kms_Travel <= 0:
                    print("Kms travelled for work must be greater than 0 kms - please re-enter")
                elif Kms_Travel > 1000:
                    Vehicle_Payout = Kms_Travel * (PER_KM_RATE)
                    Msg = "Mileage Amount:"
                    Kms_Msg = "kms Traveled:"
                    Kms_TravelDsp = "{:.2f}".format(Kms_Travel)
                    break
                else:  # int(Kms_T) < 1000:
                    Vehicle_Payout = Kms_Travel * PER_KM_RATE
                    Msg = "Mileage Amount:"
                    Kms_Msg = "kms Traveled:"
                    Kms_TravelDsp = "{:.2f}".format(Kms_Travel)
                    break

        # Input and validation of claim type
        while True:
            Allowed_Char = set("SE")
            Claim_Type = input("Enter claim type Standard or Executive (S or E):     ").upper()
            if Claim_Type == "":
                print("Claim type can't be blank - please re-enter")
            elif set(Claim_Type).issubset(Allowed_Char) == False:
                print("Claim type cannot contain invalid characters - please re-enter")
            else:
                break

        # Below are all the values needed to calculate the bonus
        # Calculate bonus rate for days bonus
        if Num_Days > 3:
            Days_Amt_Bonus = BONUS_DAYS_AMOUNT
        else:
            Days_Amt_Bonus = 0

        # Calculation bonus if kms is over 1000

        if Vehicle_Type == "R":
            Kms_Bonus = 0
        elif Vehicle_Type == "O" and Kms_Travel > 1000:
            Kms_Bonus = Kms_Travel * (BONUS_KM_RATE)
        else:
            Kms_Bonus = 0

        # Calculate bonus rate for executive claims
        if Claim_Type == "S":
            Claim_Type_Bonus = 0
            Claim_TypeDsp = "STANDARD"
        else:
            Claim_Type_Bonus = Num_Days * EXECUTIVE_RATE
            Claim_TypeDsp = "EXECUTIVE"

        # Calculate start and end date bonus for December
        SD_Date = Start_Date
        Start_Date_Year = SD_Date.year
        Start_Date_Month = 12
        Start_Date_Day = 15
        SD_Date = datetime.datetime(Start_Date_Year, Start_Date_Month, Start_Date_Day)

        ED_Date = End_Date
        End_Date_Year = ED_Date.year
        End_Date_Month = 12
        End_Date_Day = 22
        ED_Date = datetime.datetime(End_Date_Year, End_Date_Month, End_Date_Day)

        if Start_Date >= SD_Date and End_Date <= ED_Date:
            Special_Dates_Bonus = Num_Days * DEC_BONUS_RATE
        else:
            Special_Dates_Bonus = 0

        # Calculating the bonus
        Bonus_Total = Days_Amt_Bonus + Kms_Bonus + Claim_Type_Bonus + Special_Dates_Bonus

        # Calculating per diem amount
        Per_Diem = Num_Days * DAILY_RATE

        # Calculating tax
        Tax = Per_Diem * HST

        # Calculating claim amount
        Claim_Amount = Per_Diem + Vehicle_Payout + Bonus_Total

        # Calculate total claim including tax
        Total_Claim = Claim_Amount + Tax

        # This calls the def dollar_format function to format anything that is a dollar value

        DF = Dollar_Format

        # Formatting for final display
        TaxDsp = DF(Tax)
        Claim_AmountDsp = DF(Claim_Amount)
        Total_ClaimDsp = DF(Total_Claim)
        Vehicle_PayoutDsp = DF(Vehicle_Payout)
        Per_DiemDsp = DF(Per_Diem)
        Days_Amt_BonusDsp = DF(Days_Amt_Bonus)
        Kms_BonusDsp = DF(Kms_Bonus)
        Claim_Type_BonusDsp = DF(Claim_Type_Bonus)
        Special_Dates_BonusDsp = DF(Special_Dates_Bonus)
        Bonus_TotalDsp = DF(Bonus_Total)
        Start_DateDsp = Start_Date.strftime("%d-%b-%y")
        End_DateDsp = End_Date.strftime("%d-%b-%y")


        # Display of all inputs and calculated values

        print()
        print()
        print()
        print("-" * 38)
        print(" " * 7, "YOUR CLAIMS STATEMENT")
        print("-" * 38)
        print("{:<25} {:<5}".format("Employee Number:", Emp_Num))
        print("{:<25} {:<12}".format("Employee First Name:", First_Name))
        print("{:<25} {:<12}".format("Employee Last Name:", Last_Name))
        print("{:<25} {:<12}".format("Location Traveled:", Location))
        print("{:<25} {:<9}".format("Travel Start Date:", Start_DateDsp))
        print("{:<25} {:<9}".format("Travel End Date:", End_DateDsp))
        print("{:<25} {:<16}".format("Vehicle Type Used:", Vehicle_Type_Selected))
        print("{:<25} {:<12}".format("Claim Type Selected:", Claim_TypeDsp))
        print("{:<25} {:<3}".format("Trip Duration:", str(Num_Days) + " days"))
        print("{:<25} {:<7}".format(Kms_Msg, Kms_TravelDsp))
        print()
        print("-" * 38)
        print(" " * 10, "Bonus Breakdown")
        print("-" * 38)
        print("{:<28} {:>9}".format("Away 3 Days or More:", Days_Amt_BonusDsp))
        print()
        print("{:<54} {:>6}".format("Traveled over 1000 kms\n(Personal Vehicle Only):", Kms_BonusDsp))
        print()
        print("{:<45} {:>9}".format("Claim Type Bonus\n(Executive Claim Only):", Claim_Type_BonusDsp))
        print()
        print("{:<43} {:>9}".format("December Bonus\n(Between Dec 15-22):", Special_Dates_BonusDsp))
        print(" " * 26, "-" * 11)
        print("{:<28} {:>9}".format("Total Bonus:", Bonus_TotalDsp))
        # maybe take out "Total Bonus" as its displayed lower down in the subtotal
        print()
        print("-" * 38)
        print(" " * 12, "Claim Amount")
        print("-" * 38)
        print("{:<30} {:>7}".format("Per Diem Amount:", Per_DiemDsp))
        print("{:<30} {:>7}".format("Total Bonus:", Bonus_TotalDsp))
        print("{:<30} {:>7}".format(Msg, Vehicle_PayoutDsp))
        print(" " * 26, "-" * 11)
        print("{:<28} {:>9}".format("Claim Amount:", Claim_AmountDsp))
        print()
        print("-" * 38)
        print(" " * 12, "Total Claim")
        print("-" * 38)
        print("{:<28} {:>7}".format("Claim Amount:", Claim_AmountDsp))
        print("{:<30} {:>7}".format("HST Amount:", TaxDsp))
        print(" " * 26, "-" * 11)
        print("{:<28} {:>9}".format("Claim Total:", Total_ClaimDsp))
        print()

        while True:
            Continue = input("Do you want to process another claim (Y / N): ").upper()
            print()
            if Continue != "Y" and Continue != "N":
                print("Not Valid Try Again")
            else:
                break
        if Continue == "N":
            break

# User choices
def User_Choices():

    while True:
        Display_Menu()
        Choice = input("Enter choice: (1-5): ")
        print()
        if Choice == "1":
            Emp_Trav_Claim()
        # elif Choice == "2":
        #     Fun_Question()
        # elif Choice == "3":
        #     Strings_Dates()
        # elif Choice == "4":
        #     Graph_Monthly_Totals()
        elif Choice == "5":
            print("Thank you for utilizing the \"Claims Processing System\", have a wonderful day.")
            break
        else:
            print("Not a valid choice - please re-enter")
            print()

# The programs is the main that calls the user chooses menu.
# Without it the other functions listed would not return to the menu for another user choice.
# In all the main user functions there is an exit(User_Choice()) used to return to
# and present the user options again

User_Choices()