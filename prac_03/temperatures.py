"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_celsius():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def convert_to_fahrenheit():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = float(input(5 / 9 * (fahrenheit - 32)))
    print("Result: {:.2f} C".format(celsius))


while choice != "Q":
    if choice == "C":
        convert_to_celsius()
    elif choice == "F":
        convert_to_fahrenheit()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

