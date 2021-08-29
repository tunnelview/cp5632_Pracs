
def main():
    user_score = int(input("Please Enter Your Score: "))
    print(check_your_status(user_score))

def check_your_status(user_score):
    if user_score < 0 or user_score > 100:
        return "Invalid score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
