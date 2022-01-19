from prac_06.guitar import Guitar

def main():

    list_of_guitars = []

    print("My list_of_guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar1 = Guitar(name, year, cost)
        list_of_guitars.append(guitar1)
        name = input("Name: ")

    list_of_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    list_of_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if list_of_guitars:
        print("This is my list_of_guitars:")
        for i, guitar in enumerate(list_of_guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))



main()