"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of num_months."""
    incomes = []
    num_months = int(input("How many number of months? "))

    for month in range(1, num_months+1):
        income = float(input("Enter income for month " .format(str(month)) .format(": ")))
        incomes.append(income)

    income_final_report(incomes, num_months)


def income_final_report(incomes, num_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()




#Questions & Answers
#Q1- We need a list to store the incomes.How do you add values to a list?
#A1- We are using the append function to add value to the list.

#Q2 - How many loops will we need? What kind of loops?
#A2- Two loops, one to insert or append the month value in list
# and 2nd to show or iterate month data (show value of each month
# and addition of each iteration).



#
