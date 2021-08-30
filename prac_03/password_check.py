

def main():

    MINIMUM_LENGTH = 16

    get_password(MINIMUM_LENGTH)


def get_password(MINIMUM_LENGTH):
    get_password = input("Enter Password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(get_password) < MINIMUM_LENGTH:
        print(f"please enter password of {MINIMUM_LENGTH} characters")
        get_password = input("Enter Password of at least {} characters: ".format(MINIMUM_LENGTH))
    print_pwd(get_password)


def print_pwd(get_password):
    print("*" * len(get_password))


# if len(get_password) < 10:
#
# elif len(get_password) > 10 :
#     print("Your password is too long, try again!")
# else:
#     print("Your password length is correct")
# print("Your password is masked")


main()
