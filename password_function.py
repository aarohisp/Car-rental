from crossroads import password_fn


def password(x, city):
    ans = input("enter is this your first time in our website?(y/n): ")
    if ans == "y" or ans == "yes":
        password_fn.create_password(x, city)
    elif ans == "n" or ans == "no":
        password_fn.check_password(x, city)
    else:
        print("please enter one of the given options")
        answer = input("would you like to enter your choice again?")
        if answer == "y" or answer == "yes":
            password(x, city)
        else:
            print("thank you for using our system")
            exit()
