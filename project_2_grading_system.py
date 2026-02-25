# Project 2: Grading System
# Takes student marks as input and returns the corresponding grade
# Built with Python using if/elif/else conditionals

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif marks >= 85:
    print("Result: A+ (Excellent)")
elif marks >= 75:
    print("Result: B+ (Good)")
elif marks >= 65:
    print("Result: C+ (Average)")
elif marks >= 50:
    print("Result: D+ (Below Average)")
elif marks >= 40:
    print("Result: D (Pass)")
else:
    print("Result: F (Failed)")
