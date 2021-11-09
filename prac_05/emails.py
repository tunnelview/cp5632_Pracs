
EMAIL_ADDRESS_TO_NAME = {"shibin.abraham@gmail.com": "Shibin Abraham", "digitallearning@gmail.com": "Andrew",
                 "shona@gmail.com": "Shibin","shining@gmail.com": "Shibin"}


def main():
    email_address = input("Email: ")
    while email_address != "":
        name = name_from_email(email_address)
        user_response = input("Is your name {}? (Y/n) ".format(name))
        if user_response.upper() != "Y" and user_response != "":
            name = input("Name: ")
        EMAIL_ADDRESS_TO_NAME[email_address] = name
        email_address = input("Email: ")

    for email_address, name in EMAIL_ADDRESS_TO_NAME.items():
        print("{} ({})".format(name, email_address))


def name_from_email(email):
    first_part = email.split('@')[0]
    parts = first_part.split('.')
    user_name = " ".join(parts).title()
    return user_name

main()