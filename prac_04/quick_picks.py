
import random

def main():
    """Quick picks program - choose sets of random numbers."""
    quick_picks = int(input("How many quick_picks would you like? "))
    while quick_picks <= 0:
        print("You entered a wrong value, try again!")
        quick_picks = int(input("How many quick picks would you like? "))

    for k in range(quick_picks):
        quick_pick = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in quick_pick:
                number = random.randint(1, 45)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()


