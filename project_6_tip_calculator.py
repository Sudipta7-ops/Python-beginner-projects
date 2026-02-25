# Project 6: Tip Calculator
# Calculates tip amount and total bill based on user input
# Built with Python using functions and f-strings

def get_bill_amount():
    return float(input("Enter your bill amount ($): "))

def get_tip_percentage():
    return float(input("Enter tip percentage (e.g. 10 for 10%): "))

def calculate_tip(bill, tip_percentage):
    return bill * (tip_percentage / 100)

def calculate_total(bill, tip):
    return bill + tip

bill = get_bill_amount()
tip_percentage = get_tip_percentage()
tip = calculate_tip(bill, tip_percentage)
total = calculate_total(bill, tip)

print(f"\nBill Amount : ${bill:.2f}")
print(f"Tip Amount  : ${tip:.2f}")
print(f"Total Bill  : ${total:.2f}")
