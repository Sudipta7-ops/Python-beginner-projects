# Project 3: Simple Calculator
# Performs basic arithmetic operations on two numbers
# Built with Python using functions and f-strings

num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
