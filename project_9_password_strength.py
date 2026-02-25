# Project 9: Password Strength Checker
# Evaluates the strength of a password based on length, characters, and symbols
# Built with Python using functions and the any() built-in

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if any(char in "!@#$%^&*()_-+=[]{};:'\",.<>?/" for char in password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$% etc.).")

    if strength == 5:
        result = "Strong Password"
    elif 3 <= strength < 5:
        result = "Moderate Password"
    else:
        result = "Weak Password"

    return result, feedback


user_password = input("Enter your password: ")
result, tips = check_password_strength(user_password)

print(f"\nPassword Strength: {result}")
if tips:
    print("Tips to improve:")
    for tip in tips:
        print(f"  - {tip}")
