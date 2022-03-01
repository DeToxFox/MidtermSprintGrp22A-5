import datetime

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
        # input and validation of the employee number
        Emp_Num = input("Please enter in your 5 digit employee numer (12345):  ")
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
        FirstName = input("Enter the your first name (type End to exit): ").title()
        if FirstName == "End":
            exit()
        elif FirstName == "":
            print("First name must not be blank - please re-enter.")
        elif set(FirstName).issubset(Allowed_Char) == False:
            print("First name contains invalid characters - please re-enter")
        else:
            break

    # Input and validation of the employee's last name
    while True:
        Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890-'")
        LastName = input("Enter the your last name: ").title()
        if LastName == "":
            print("Last name must not be blank - please re-enter.")
        elif set(LastName).issubset(Allowed_Char) == False:
            print("Last name contains invalid characters - please re-enter")
        else:
            break

    # Input and validation for the employee trip location
    while True:
        Allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'")
        Location = input("Enter the trip location: ").title()
        if Location == "":
            print("Trip location can't be blank - please re-enter")
        elif set(Location).issubset(Allowed_Char) == False:
            print("Trip locatiopn cannot contain invalid characters - please re-enter")
        else:
            break

    # Input and validation for the employee trip distance
    while True:
        try:
            StartDate = input("Enter the start date of the claim (YYYY-MM-DD): ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print("Start date not a valid format - please re-enter.")
        else:
            break
    while True:
        try:
            EndDate = input("Enter the end date of the claim (YYYY-MM-DD): ")
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
        Vehicle_Type = input("Enter the vehicle used, own or rental (O or R): ").upper()
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
        Vehicle_Payout = NumDays * RENTAL_CAR_RATE
        Msg = "The Rental Payout is "
    elif Vehicle_Type == "O":
        while True:
            try:
                Kms_Travel = float(input("How many kms where traveled on the work trip?: "))
            except:
                print("Trade in value is not a valid number - please re-enter.")
            if Kms_Travel > 2000:
                print("Kms travelled for work must be under 2000 kms - please re-enter")
            elif Kms_Travel <= 0:
                print("Kms travelled for work must be greater than 0 kms - please re-enter")
            elif Kms_Travel > 1000:
                Vehicle_Payout = Kms_Travel * (PER_KM_RATE)
                Msg = "Your travel pay "
                KMP = f"The kms traveled {Kms_Travel:.2f}"
                break
            else:  # int(Kms_T) < 1000:
                Vehicle_Payout = Kms_Travel * PER_KM_RATE
                Msg = "Your travel pay "
                KMP = f"The kms traveled {Kms_Travel:.2f}"
                break

    # Input and validation of claim type
    while True:
        Allowed_Char = set("SE")
        Claim_Type = input("Enter claim type Standard or Executive (S or E): ").upper()
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
        MemberTypeDsp = "STANDARD"
    else:
        Claim_Type_Bonus = NumDays * EXECUTIVE_RATE
        ClaimTypeDsp = "EXECUTIVE"

    # Calculate start and end date bonus
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
    Bonus = Days_Amt_Bonus + Kms_Bonus + Claim_Type_Bonus + Special_Dates_Bonus

    # Calculating per diem amount
    Per_Diem = NumDays * DAILY_RATE

    # Calculating tax
    Tax = Per_Diem * HST

    # Calculating claim amount
    Claim_Amount = Per_Diem + Vehicle_Payout + Bonus

    # Calculate total claim including tax
    Total_Claim = Claim_Amount + Tax

    # Formatting for final display
    VPDsp = "${:,.2f}".format(Vehicle_Payout)
    Per_DiemDsp = "${:,.2f}".format(Per_Diem)

    print()

    # Display of all inputs and calculated values

    print("3 days or more bonus", Days_Amt_Bonus)
    print("1000 plus kms bonus", Kms_Bonus)
    print("Executive Claim Bonus", Claim_Type_Bonus)
    print("December bonus", Special_Dates_Bonus)
    print("This is total bonus", Bonus)

    # Testing purposes origianally possibly delete later
    print("Per Diem: ", Per_DiemDsp)
    print(Msg, VPDsp)
    print(KMP)

    while True:
        Continue = input("Do you want to process another claim (Y / N): ").upper()
        print()
        if Continue != "Y" and Continue != "N":
            print("Not Valid Try Again")
        else:
            break
    if Continue == "N":
        exit()