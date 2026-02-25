# Project 1: Bio Generator
# Takes user input and generates a short personal bio
# Built with Python using basic input/output and f-strings

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")
fact = input("Tell me a fun fact about you: ")

print("\n--- Your Bio ---")
print(f"Hi, I am {name}.")
print(f"I am {age} years old and I live in {city}.")
print(f"Fun fact about me: {fact}.")
