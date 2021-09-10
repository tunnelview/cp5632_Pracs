from prac_06.guitar import Guitar

def main():
    guitar_one = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar_one.name, 95,
                                                      guitar_one.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 5,
                                                      other_guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar_one.name,
                                                         True,
                                                         guitar_one.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other_guitar.name,
                                                         False,
                                                         other_guitar.is_vintage()))

main()


