import math

'''
This is one of the programs I developed during my bootcamp and it asks to create a calculator that 
calculates the interest gained on investments (simple or compound) based on the deposit, the interest rate, 
and the amount of years you want to invest for.
It also calculates the amount to repay per month on a bond based on the price of the bond, the interest rate, 
and on how many months you would like to repay it for.

Pseudo code:

- ask the user which calculator they want to use
- after selection, ask user for the variables needed
    - if investments ask for the amount of the deposit, interste rate, and how many years to invest for
        - ask user if it is simple or compound and shows the amount
    - if bond select, ask for the price of the bond, interest rate, and how many months to pay it for
        - shows the amount to be paid per month and how many months to pay it for
- if wrong answer entered, inform user and ask if they want to try again
- if 'no' is entered then the program ends, otherwise, show main menu again

'''

def bond_repayment_calc( interest, house_value, repaying_months) :
    return (interest * house_value) / (1 - (1 + i)**(1 - (repaying_months + 1)))

menu = True

# while menu is true, the menu will keep repeating
while menu :

    # asks the user which calculator to use

    calculator = input(f'''\n\nWhich calculator would you like to use?
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: ''').lower()
    
    # depending on the user's answer, it picks the calculator to be used
    if calculator == "investment" :

        deposit = float(input("\n\nHow much is your deposit? "))
        interest_rate = float(input("Please enter the interest rate (in percentage %): "))
        investing_years = int(input("How many years do you want to invest for? "))
        interest = input("Which type of interest do you want to apply ('simple' or 'compound')?: ").lower()

        r = interest_rate / 100

        if interest == "simple" :
            
            a = deposit * (1 + r * investing_years)
            print(f"After {investing_years} years investing with {interest_rate}% of interest rate, you would would have £{a:.2f}.\n")

        if interest == "compound" :

            a = deposit * math.pow((1 + r),investing_years)
            print(f"After {investing_years} years investing with {interest_rate}% of interest rate, you would would have £{a:.2f}.\n")
    
        repeat = input("Would you like to go to the main menu? Enter 'Yes' or 'No': ").lower()
        if repeat == "no" :
            menu = False

    elif calculator == "bond" :

        house_value = float(input("\n\nEnter the value of the house: "))
        interest_rate = float(input("Enter the value for the interest rate (in percentage %): "))
        repaying_months = int(input("In how many months do you want to repay your bond? "))

        i = (interest_rate / 100) / 12
        
        repayment = bond_repayment_calc(i,house_value,repaying_months) #(i * house_value) / (1 - (1 + i)**(1 - (repaying_months + 1)))

        print(f"\nThe amount that you will have to repay on a home loan each month is £{repayment:.2f} for {repaying_months} months.")

        repeat = input("\n\nWould you like to go to the main menu? Enter 'Yes' or 'No': ").lower()
        if repeat == "no" :
            menu = False

    else :
        repeat = input("That is neither of the options given. Want to try again? Enter 'Yes' or 'No': ").lower()
        if repeat == "no" :
            menu = False

print("Have a nice day! Goodbye.")
