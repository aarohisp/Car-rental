from crossroads import password_function


def choice(city):
    global x
    try:
        x = int(input('''please choose your choice of action:
1. rent a car       2.rent out/lend your car     3.cancel reservation       4.exit
enter: '''))
    except:
        print("please enter one of the given options ")
        choice(city)
    if int(x) == 1:
        password_function.password(x, city)
    elif int(x) == 2:
        password_function.password(x, city)
    elif int(x) == 4:
        print("thank you for using our system")
        exit()
    elif int(x) == 3:
        password_function.password(x, city)
    else:
        print("please enter one of the given options")
        answer = input("would you like to enter your choice again?")
        if answer == "y" or answer == "yes":
            choice(city)
        else:
            print("thank you for using our system")
            exit()
