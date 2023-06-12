#SEL1T11 Capstone Project 1 - Variables and Control Structures

#Import Math Library
import math

#r = (rate_interest / 100 ) / 12
# User select and input
print("\nPlease choose your type financial service: 'Investment' or 'bond';\n\nInvestment - to calculate the amount of intrest you will earn on your investment \nBond - to calculate the amount you will have to pay on a home loan\n")
#user to select a type of product: 
select_service = str(input("Please enter: \nInvestment or Bond: ")).capitalize()

# Investment option
if select_service == "Investment":
    if True:
        principal_invest = float(input("Please enter the your principal amount you wish to invest: \n"))
        rate_interest = float(input("Please enter the interest rate amount: \n"))
        r = (rate_interest / 100 ) / 12
        time_invest = float(input("Please enter the total number of years you wish to invest for e.g 5, 10, 15, 20: "))
    interest = str(input("Please enter: \nSimple or Compound: ")).capitalize()
# if statement condition based on the simple and compound calcutations 
    if interest == "Simple": 
        interest = principal_invest * (1 + r * time_invest)
        print("Your interest that will be earn over %0.2f" %time_invest, "years will be R%0.2f" %interest)
        total = principal_invest + interest
        print("Your total payout after %0.0f" %time_invest, " years will be R%0.2f" %total)  
    elif interest == "Compound": 
        interest = principal_invest * math.pow(( 1 + r ), time_invest)
        print("Your interest that will be earned over %0.2f" %time_invest, "years will be R%0.2f" %interest)
        total = principal_invest + interest
        print("Your total payout after %0.0f" %time_invest, "years will be R%0.2f" %total)
# if statement to calculate the bond option
elif select_service == "Bond":
    if True:
        bond_house_val = float(input("Please enter your home's current market value: \n"))
        bond_rate_interest = float(input("Please enter the interest rate amount: \n"))
        i = (bond_rate_interest / 100 ) / 12
        bond_term = float(input("Please enter the bond term in months e.g \n10 years = 120 months, \n15 years = 180 months, \n20 years = 240 months, \n30 years = 360 months: \nMonths: "))
        repay = float(math.floor( i * bond_house_val) / (1 - (1 + i ) ** (- bond_term)))
        print("Your monthly repayment will be: R%0.2f" %repay, "for %0.0f months" %bond_term, "at %0.2f percent" %bond_rate_interest )
else:
    print("Oh No! Let's try it again")
