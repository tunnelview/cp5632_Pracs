"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if (denominator ==0):
        print("Please enter a value greater than zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1.When will a ValueError occur?
# Value error will occur if the data type is mismatched, i.e if the user
# keys in a string or character instead of a int.

# 2. When will a ZeroDivisionError occur?
# When we divide any integer by zero

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, we can. We can set up a condition for the user to key in a
# value greater than zero.


