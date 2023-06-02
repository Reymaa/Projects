#Affordable Housing

##### Defines a function tht calculates after tax income.
def calculate_after_tax_income(gross_income):
    # Define the tax brackets and their respective percentages
    tax_brackets = {
        0: 0.10,
        9875: 0.12,
        40125: 0.22,
        85525: 0.24,
        163300: 0.32,
        207350: 0.35,
        518400: 0.37
    }
    
    # Calculate the after-tax income
    remaining_income = gross_income
    tax_amount = 0
    
    for limit, tax_rate in tax_brackets.items():
        if remaining_income > limit:
            taxable_amount = remaining_income - limit
            tax_amount += taxable_amount * tax_rate
            remaining_income -= taxable_amount
    
    after_tax_income = gross_income - tax_amount
    return after_tax_income

#####
def calculate_income_required(rentAmount):
    atRate = float((10/3))
    atIncomeReq = rentAmount * atRate
    return atIncomeReq

#####

#####
try:
    rentAmount = float(input('Enter monthly rent amount: '))
except ValueError:
    while True:
        try:
            rentAmount = int(input('Invalid input! Please enter a dollar value for rent amount: '))
            break  # Break out of the loop if a valid integer is entered
        except ValueError:
            print('Invalid input! Please try again.')

try:
    gross_income = float(input('Enter yearly gross income: '))
except ValueError:
    while True:
        try:
            gross_income = int(input('Invalid input! Please enter a dollar value for gross income: '))
            break  # Break out of the loop if a valid integer is entered
        except ValueError:
            print('Invalid input! Please try again.')

#####
aft_income_req = calculate_income_required(rentAmount * 12)
aft_Tax_income = calculate_after_tax_income(gross_income)
aft_tax_rent_rate = (rentAmount / (aft_Tax_income / 12))
affordableHousingRate = 0.3
biweekly_paycheck = (aft_income_req / 26)

##### What a person would actaully be able to afford based on their inputted gross income.
affordableRent = (aft_Tax_income /12) * affordableHousingRate
##gross_income_req = ###

#####
if aft_tax_rent_rate <= affordableHousingRate:
    print("Congratulation's you are safely able to afford this monthly rent!")
    print("You would be able to afford up to a monthly rent of ${:.2f}" .format(affordableRent))
else:
    print("You are unable to afford this monthly rent")
    print("You would safely be able to afford a monthly rent of $ {:.2f}" .format(affordableRent))
    print("You would need an AFTER TAX yearly income of $ {:.2f}" .format(aft_income_req), "for this rent to be considered affordable.")
    print("Put simply, you would need a paycheck of $ {:.2f}" .format(biweekly_paycheck), "every two weeks")