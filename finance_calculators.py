import math
import sys  # This is required to end the programme if the user enters incorrectly

# In this programme the user will be able to choose whether to use an investment or bond calculator

# Below is the variable which will take the user's option. The use of capitalising will also be used so any option
# cont.. the user inserts will be valid
user_calculator = input("""Choose either 'Investment' or 'Bond' from the menu below to proceed: 
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan
""").capitalize()

if user_calculator == "Investment":
    # if 'investment' is chosen, the programme will request the below inputs
    # I have included 'I' on each of the investment variables, incase I need to make a similar named variable
    # (cont) for the other calculator
    user_depositI = float(input("Enter the amount of money you are depositing ")) # Float required for more calculations
    user_interestI = float(input("Enter interest rate (do not include %) "))  # As above regarding Float
    user_yearsI = float(input("Enter the number of years planned on investing "))
    interest_I = input("Confirm 'Simple' or 'Compound' interest ").capitalize() # Capitalised for calcs later on
    # Below is calculation of the simple or compound interest option for the investment option
    if interest_I == "Simple":
        simple_I = user_depositI * (1 + (user_interestI / 100) * user_yearsI)  # This is the total, including interest
    elif interest_I == "Compound":
        compound_I = user_depositI * math.pow((1 + (user_interestI / 100)), user_yearsI)
    else:
        sys.exit("You have entered an incorrect option. Please start again")  # Error and end of programme


elif user_calculator == "Bond":
    user_housevalueB = float(input("Enter value of house (Do not include £/$/R) "))  # Float as decimals will be used
    user_interestB = float(input("Enter the annual interest rate (do not include %) ")) # Float as above
    user_monthsB = float(input("Enter months planned to repay the bond "))  # Float so calculations can be used
else:
    sys.exit("You have entered an incorrect option. Please start again")
    # Exit message and exit/end of programme for incorrect input from user


# Below is the results for all the different options that the user could have given, using 'elifs'
if user_calculator == "Investment" and interest_I == "Simple":
    print("The amount of interest you will earn on your investment is:")
    print(round(simple_I - user_depositI))  # The original deposit needs to be subtracted to know just the interest
elif user_calculator == "Investment" and interest_I == "Compound":
    print("The amount of interest you will earn on your investment is:")
    print(round(compound_I - user_depositI))  # The original deposit needs to be subtracted to know just the interest
elif user_calculator == "Bond":
    print("The amount you will have to pay on a home loan is:")
    print(round(((user_interestB/12) * user_housevalueB)/(1 - ((1 + user_interestB)**(-user_monthsB)))))
    # user_interestB divided by 12 to get monthly interest rate rather than annually
    # This formula does not appear to be working as i am not familiar with the South African Bond repayment calculations
    # However, I believe the principal of the programme is correct and a small tweak to line 48 will resolve it










