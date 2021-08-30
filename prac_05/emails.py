
EMAIL_ADDRESS = {"shibin.abraham@gmail.com": "Shibin", "digitallearning@gmail.com": "Arvind",
                 "shona@gmail.com": "Shibin","shining@gmail.com": "Shibin"}


user_email = input("Email: ")
while user_email != "":
    if user_email in EMAIL_ADDRESS.keys():
        # print(user_email, "name is", EMAIL_ADDRESS.get(user_email))
        print("Is your name", EMAIL_ADDRESS.get(user_email),"? (Y/n)")
        str = input()
        if str == "n":
            name = input("Name: ")
        elif str == "Y":
            pass
        else:
            pass
    else:
        print("User Email Not Found")
    user_email = input("Email: ")

for emails, names in EMAIL_ADDRESS.items():
    print(names,"(",emails,")")
