# Employee Claims Processing System (work trips) at the NL Chocolate Company

# Written by: Group 22A-5, Makenzie Roberts, Neil Stratton, and David Turner
# Date written: Feb 26, 2022
# Project ID: Midterm Sprint Week. Project 1: NL Chocolate Company, Claims Processing System

# Libraries imported

import matplotlib.pyplot as plt
import datetime
import random

def Display_Menu():
    print("NL Chocolate Company Claims Processing System")
    print("-"*46)
    print("Enter an Employee Travel Claim - Press 1")
    print("Fun Interview Question  - Press 2")
    print("Cool Stuff with Strings and Dates - Press 3")
    print("Graph Monthly Claim Totals - Press 4")
    print("Quit the Program - Press 5")
    print()


def dollar_format(num):

    # Written By: Makenzie Roberts
    # Last Edited: Feb 28, 2022

    # Description:
    #   This function formats a numerical value to display as a dollar value.

    # Parameters:
    #   The numerical value that will be formatted.

    # Returns:
    #   Returns the numerical value as a string, formatted to look like a dollar value.
    #   Eg. The argument 123456 is returned as $123,456.00

    formatStr = "{:,.2f}".format(num)

    return formatStr


def Emp_Trav_Claim():

    # Written By: David Turner
    # Last Edited: Mar 1, 2022

    # Description:
    #   This function allows an employee to enter as many travel claims as needed.

    # Parameters:
    # A parameter is the variable listed inside the parentheses in the function definition.
    #
    # An argument is the value that is sent to the function when it is called.

    # Returns:
    #   There is no return with this function as the display is
    #   completed and output presented prior to returning to main


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
        while True:
            # Welcome message
            print()
            print("       ------------------------------------")
            print("         Option 1: Employee Travel Claim")
            print("       ------------------------------------")
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
            FirstName = input("Enter the your first name (type End to exit):        ").title()
            if FirstName == "End":
                break
            elif FirstName == "":
                print("First name must not be blank - please re-enter.")
            elif set(FirstName).issubset(Allowed_Char) == False:
                print("First name contains invalid characters - please re-enter")
            else:
                break

        # Input and validation of the employee's last name
        while True:
            Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890-'")
            LastName = input("Enter the your last name:                            ").title()
            if LastName == "":
                print("Last name must not be blank - please re-enter.")
            elif set(LastName).issubset(Allowed_Char) == False:
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
                print("Trip locatiopn cannot contain invalid characters - please re-enter")
            else:
                break

        # Input and validation for the employee trip distance
        while True:
            try:
                StartDate = input("Enter the start date of the claim (YYYY-MM-DD):      ")
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            except:
                print("Start date not a valid format - please re-enter.")
            else:
                break
        while True:
            try:
                EndDate = input("Enter the end date of the claim (YYYY-MM-DD):        ")
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            except:
                print("End date not a valid format - please re-enter.")
            else:
                if EndDate <= StartDate:
                    print("End date must be after the start date - please re-enter.")
                else:
                    # Calculate the number of days of the claim and ensure number of days doesn't exceed 7,
                    # will become the Other function possibly
                    NumDays = (EndDate - StartDate).days
                    if NumDays > 7:
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

        # Calculations for the vehicle allowance, rental or own vehicle
        Vehicle_Payout = 0
        Msg = ""
        KMP = ""
        Vehicle_Payout_Bonus = 0

        if Vehicle_Type == "R":
            Vehicle_Type_Selected = "Rental"
            Vehicle_Payout = NumDays * RENTAL_CAR_RATE
            Msg = "Rental Amount:"
        elif Vehicle_Type == "O":
            Vehicle_Type_Selected = "Personal"
            while True:
                try:
                    Kms_Travel = float(input("How many kms were traveled on the work trip?:        "))
                except:
                    print("Trade in value is not a valid number - please re-enter.")
                if Kms_Travel > 2000:
                    print("Kms travelled for work must be under 2000 kms - please re-enter")
                elif Kms_Travel <= 0:
                    print("Kms travelled for work must be greater than 0 kms - please re-enter")
                elif Kms_Travel > 1000:
                    Vehicle_Payout = Kms_Travel * (PER_KM_RATE)
                    Msg = "Mileage Amount:"
                    KMP = f"The kms traveled {Kms_Travel:.2f}"
                    break
                else:  # int(Kms_T) < 1000:
                    Vehicle_Payout = Kms_Travel * PER_KM_RATE
                    Msg = "Mileage Amount:"
                    KMP = f"The kms traveled {Kms_Travel:.2f}"
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
        if NumDays > 3:
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
            ClaimTypeDsp = "STANDARD"
        else:
            Claim_Type_Bonus = NumDays * EXECUTIVE_RATE
            ClaimTypeDsp = "EXECUTIVE"

        # Calculate start and end date bonus for December
        SDDate = StartDate
        Start_Date_Year = SDDate.year
        Start_Date_Month = 12
        Start_Date_Day = 15
        SDDate = datetime.datetime(Start_Date_Year, Start_Date_Month, Start_Date_Day)

        EDDate = EndDate
        End_Date_Year = EDDate.year
        End_Date_Month = 12
        End_Date_Day = 22
        EDDate = datetime.datetime(End_Date_Year, End_Date_Month, End_Date_Day)

        if StartDate >= SDDate and EndDate <= EDDate:
            Special_Dates_Bonus = NumDays * DEC_BONUS_RATE
        else:
            Special_Dates_Bonus = 0

        # Calculating the bonus
        Bonus_Total = Days_Amt_Bonus + Kms_Bonus + Claim_Type_Bonus + Special_Dates_Bonus

        # Calculating per diem amount
        Per_Diem = NumDays * DAILY_RATE

        # Calculating tax
        Tax = Per_Diem * HST

        # Calculating claim amount
        Claim_Amount = Per_Diem + Vehicle_Payout + Bonus_Total

        # Calculate total claim including tax
        Total_Claim = Claim_Amount + Tax

        # Formatting for final display
        TaxDsp = "${:,.2f}".format(Tax)
        Claim_AmountDsp = "${:,.2f}".format(Claim_Amount)
        Total_ClaimDsp = "${:,.2f}".format(Total_Claim)
        Vehicle_PayoutDsp = "${:,.2f}".format(Vehicle_Payout)
        Per_DiemDsp = "${:,.2f}".format(Per_Diem)
        Days_Amt_BonusDsp = "${:,.2f}".format(Days_Amt_Bonus)
        Kms_BonusDsp = "${:,.2f}".format(Kms_Bonus)
        Claim_Type_BonusDsp = "${:,.2f}".format(Claim_Type_Bonus)
        Special_Dates_BonusDsp = "${:,.2f}".format(Special_Dates_Bonus)
        Bonus_TotalDsp = "${:,.2f}".format(Bonus_Total)
        StartDateDsp = StartDate.strftime("%d-%b-%y")
        EndDateDsp = EndDate.strftime("%d-%b-%y")

        # Display of all inputs and calculated values
        print()
        print()
        print()
        print("-" * 38)
        print(" " * 7, "YOUR CLAIMS STATEMENT")
        print("-" * 38)
        print("{:<25} {:<5}".format("Employee Number:", Emp_Num))
        print("{:<25} {:<12}".format("Employee First Name:", FirstName))
        print("{:<25} {:<12}".format("Employee Last Name:", LastName))
        print("{:<25} {:<12}".format("Location Traveled:", Location))
        print("{:<25} {:<9}".format("Travel Start Date:", StartDateDsp))
        print("{:<25} {:<9}".format("Travel End Date:", EndDateDsp))
        print("{:<25} {:<16}".format("Vehicle Type Used:", Vehicle_Type_Selected))
        print("{:<25} {:<12}".format("Claim Type Selected:", ClaimTypeDsp))
        print("{:<25} {:<3}".format("Trip Duration:", str(NumDays) + " days"))
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

def Fun_Question():

    # Fizz Buzz program
    # Neil Stratton March, 3, 2022
    # Sprint Week

    while True:

        for fizzbuzz in range(101):
            if fizzbuzz % 5 == 0 and fizzbuzz % 8 == 0:
                print("fizzbuzz")
                continue
            elif fizzbuzz % 5 == 0:
                print("fizz")
                continue
            elif fizzbuzz % 8 == 0:
                print("buzz")
                continue
            print(fizzbuzz)

        enter_new_info = input("Would you like to enter a info Y for Yes: ").upper()
        print("")

        if enter_new_info == "Y":
            continue
        else:
            break


def Strings_Dates():
    # Employee Username, Password, Email address and other info generator program.
    # Neil Stratton - March 3, 2022
    # Sprint week  - Fun wih Strings


    LINE = (f"-" * 55)

    # Display
    def display():
        print("[Employee Info Program with Username and Password Generator]")
        print("")

    # Inputs and validation:
    while True:
        display()
        while True:
            emp_phone_number = str(input("Enter employee phone number 10 digits 999-999-9999 format: ")).upper()
            length = len(emp_phone_number)
            if length == 12 \
                    and emp_phone_number[3] == "-" \
                    and emp_phone_number[7] == "-" \
                    and emp_phone_number[:3].isdigit() \
                    and emp_phone_number[4:7].isdigit() \
                    and emp_phone_number[8:].isdigit():
                print("")
            else:
                print("Invalid Phone Number")
                continue
            break

        while True:
            try:
                emp_first_name = str(input("Enter employee first name: "))
                if emp_first_name.isalpha():
                    pass
                else:
                    raise TypeError
            except TypeError:
                print("Invalid First Name")
            else:
                break

        while True:
            try:
                emp_last_name = str(input("Enter employee last name: "))
                if emp_last_name.isalpha():
                    print("")
                else:
                    raise TypeError
            except TypeError:
                print("Invalid Last Name")
            else:
                break

        while True:
            try:
                emp_start_date = str(input("Enter the employee start date : YYYY-MM-DD format: "))
                emp_start_date = datetime.datetime.strptime(emp_start_date, "%Y-%m-%d")
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
            else:
                break

        while True:
            try:
                emp_birth_date = str(input("Enter the employee Birthday : YYYY-MM-DD format: "))
                emp_birth_date = datetime.datetime.strptime(emp_birth_date, "%Y-%m-%d")
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
            else:
                break

        # Convert date to string and remove dashes and unwanted characters, so they won't be in password
        date_string = emp_start_date.strftime('%Y%m%d')
        bday_string = emp_birth_date.strftime('%Y%m%d')
        emp_phone_number_pass = emp_phone_number.replace('-', "")
        emp_first_name_pass = emp_first_name.replace("O", "")
        emp_last_name_pass = emp_last_name.replace("O", "")

        # Current date and time and convert to string
        cur_day = datetime.datetime.today()
        cur_time = datetime.datetime.now()
        cur_day_string = cur_day.strftime('%B, %d, %Y')
        cur_time_string = cur_time.strftime('%H:%M:%S')

        # Convert employee Birthdate to string and calculation age
        bday_full = emp_birth_date.strftime("%B")
        year_difference = cur_day.year - emp_birth_date.year
        days_company = emp_birth_date.day - cur_day.day

        # Username and password conversion variables
        symbols = ("%!#$@&*")
        alpha_chars = ("AaBbCcDdEeFfGgHhIiJjKkLlMmNnPpQqRrSsTtUuVvWwXxYyZz")

        # Combine first name and last name to check length for password options
        length = str(emp_first_name + emp_last_name)
        if len(length) <= 5:
            password_list = (
                        alpha_chars + emp_first_name_pass + emp_last_name_pass + date_string + bday_string + emp_phone_number_pass + symbols)
        else:
            password_list = (
                        emp_first_name_pass + emp_last_name_pass + date_string + bday_string + emp_phone_number_pass + symbols)

        # Randomize the password mix and output password length
        password_mix = random.choices(password_list, k=10)
        password_final = (password_mix[0] + password_mix[1] + password_mix[2] + password_mix[3] + password_mix[4] + \
                          password_mix[5] + password_mix[6] + password_mix[7] + password_mix[8] + password_mix[9])

        # Create username
        user_name = (f"{emp_first_name[0].title()}.{emp_last_name[0].title()}{emp_last_name[1:]}")

        # Adjust header lines depending on length of email address
        email_length = (
            f"Email Address is:     {emp_first_name.lower()}.{emp_last_name.lower()}@nlchocolatecompany.com")
        num = int(len(email_length))
        LINE = (f"-" * num)

        # Output display
        print("")
        print(f"EMPLOYEE REPORT:")
        print(f"{LINE}")
        print("Current Day and Time:")
        print(f"{LINE}")
        print(f" Today's Date is :    {cur_day_string}")
        print(f" Current Time is:     {cur_time_string}")
        print("")
        print(f"{LINE}")
        print(f"Employee Username, Password and Email Address: ")
        print(f"{LINE}")
        print(f" Username is:         {user_name}")
        print(f" Password is:         {password_final}")
        print(f" Email Address is:    {emp_first_name.lower()}.{emp_last_name.lower()}@nlchocolatecompany.com")
        print("")
        print(f"{LINE}")
        print(f"Other Employee info:")
        print(f"{LINE}")
        print(f" First name:           {emp_first_name.title()}")
        print(f" Last Name:            {emp_last_name.title()}")
        print(f" Phone Number:         {emp_phone_number}")
        print("")
        print(f" {emp_first_name.title()}'s Birthday is in {bday_full} ")
        print(f" {emp_first_name.title()} is {year_difference} Years old")
        print("")
        print(f"{LINE}")

        enter_new_info = input("Would you like to enter a info Y for Yes: ").upper()
        print("")
        if enter_new_info == "Y":
            continue
        else:
            break


def Graph_Monthly_Totals():

    # Written By: Makenzie Roberts
    # Last Edited: Feb 28, 2022

    # Description:
    #   This function produces a graph for Monthly Claim Totals (Total($) vs Month).

    # Parameters:
    #   Does not require a parameter and does not accept any arguments.
    #   To gather the data needed to plot the graph, it asks for (and requires) user input.

    # Returns:
    #   Returns a graph, created using matplotlib library.

    # Create lists that contain data for X and Y axis
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    # Y is initialized and empty so we can append user input
    y = []

    # Welcome message
    print()
    print("------------------------------------")
    print("Option 4: Graph Monthly Claim Totals")
    print("------------------------------------")
    print()
    print("This option produces a line graph using the data you provide. (Total($) vs Month)")
    print("Please enter the claim total($) for each month of the year.")

    print()
    # Ask user to input for monthly totals, then append to y axis list
    monthNum = 0
    for month in range(1, 13):
        inputOk = False
        while not inputOk:
            try:
                monthValue = int(input("Enter the amount for {}: ".format(month_list[monthNum])))
                inputOk = True
            except:
                print(
                    "The value for {} must be a valid number and cannot contain special characters. Please re-enter.".format(
                        month_list[monthNum]))
            else:
                y.append(monthValue)
                monthNum += 1

    # Abbreviates month names to first 3 characters for easy display
    monthNum = 0
    month_abbrev_list = []
    for month in range(1, 13):
        abbrev = month_list[monthNum]
        abbrev = abbrev[0:3]
        month_abbrev_list.append(abbrev)
        monthNum += 1

    # Set up the graph
    xAxis = month_abbrev_list
    yAxis = y

    plt.plot(xAxis, yAxis, color='#10a674', linestyle='-', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Total($)')
    plt.title('Monthly Claim Totals')
    plt.grid(True)

    # Prompts user to press any key to continue
    print()
    print("Close graph to return to main menu")
    input("Press any key to continue...")
    print()

    # Return/display the graph to the user
    plt.show()


# Programs main that calls all functions as the user chooses what they want

num = 0
dollar_format(num)
DF = dollar_format(num)  # this would have to be called first so it can be sent to other functions for use

#List = [] # delete if not needed/used

while True:
    Display_Menu()
    Choice = input("Enter choice: (1-5): ")
    print()
    if Choice == "1":
        Emp_Trav_Claim()
        #continue
    elif Choice == "2":
        Fun_Question()
    elif Choice == "3":
        Strings_Dates()
    elif Choice == "4":
        Graph_Monthly_Totals()
    elif Choice == "5":
        print("Thank you for utilizing the \"Claims Processing System\", have a wonderful day.")
        break
    else:
        print("Not a valid choice - please re-enter")
        print()