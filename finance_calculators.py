#SEL1T11 Capstone Project 1 - Variables and Control Structures

import math

print("\nPlease choose your type of financial service: 'Investment' or 'Bond';\n\nInvestment - to calculate the amount of interest you will earn on your investment\nBond - to calculate the amount you will have to pay on a home loan\n")

select_service = input("Please enter: Investment or Bond: ").capitalize()

if select_service == "Investment":
    principal_invest = float(input("Please enter the principal amount you wish to invest: "))
    rate_interest = float(input("Please enter the interest rate amount: "))
    time_invest = float(input("Please enter the total number of years you wish to invest for (e.g., 5, 10, 15, 20): "))

    interest = input("Please enter: Simple or Compound: ").capitalize()

    if interest == "Simple":
        r = (rate_interest / 100) / 12
        interest = principal_invest * (1 + r * time_invest)
        print("Your interest that will be earned over %.2f years will be R%.2f" % (time_invest, interest))
        total = principal_invest + interest
        print("Your total payout after %.0f years will be R%.2f" % (time_invest, total))
    elif interest == "Compound":
        r = (rate_interest / 100) / 12
        interest = principal_invest * math.pow((1 + r), time_invest)
        print("Your interest that will be earned over %.2f years will be R%.2f" % (time_invest, interest))
        total = principal_invest + interest
        print("Your total payout after %.0f years will be R%.2f" % (time_invest, total))
    else:
        print("Invalid input for interest type. Please choose either Simple or Compound.")

elif select_service == "Bond":
    bond_house_val = float(input("Please enter your home's current market value: "))
    bond_rate_interest = float(input("Please enter the interest rate amount: "))
    bond_term = float(input("Please enter the bond term in months (e.g., 10 years = 120 months, 15 years = 180 months, 20 years = 240 months, 30 years = 360 months): "))

    i = (bond_rate_interest / 100) / 12
    repay = math.floor(i * bond_house_val) / (1 - math.pow((1 + i), -bond_term))
    print("Your monthly repayment will be: R%.2f for %.0f months at %.2f percent" % (repay, bond_term, bond_rate_interest))

else:
    print("Invalid input for financial service type. Please choose either Investment or Bond.")
