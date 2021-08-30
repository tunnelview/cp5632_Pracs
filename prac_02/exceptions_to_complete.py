"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
Let's write a program that gets an integer
from the user and does not crash when a non-number is entered.
"""

finished = False
result = 0
while not finished:
    try:
        user_input = int(input("Please enter an integer value:"))
        print(user_input)
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)