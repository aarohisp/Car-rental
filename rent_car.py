import mysql.connector
import datetime
from crossroads import calendar_fn
from crossroads import billing_fn
from crossroads import choice_fn


def rent_a_car(x,city,user_id):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        car_type = input("enter the type of car you prefer(automatic/manual): ")
        start_date = input("enter start date(yyyy/mm/dd): ")
        cur_date = str(datetime.date.today())
        m = cur_date.split("-")
        n = int(m[0]) + 2
        if str(start_date) < str(cur_date):
            print("reservation not possible because of incorrect dates")
            answer = input("enter would you like to change the dates? ")
            if answer == "yes" or answer == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
        else:
            pass
        end_date = input("enter end date(yyyy/mm/dd): ")
        address = input("enter pickup point: ")
        time = input("enter pickup time: ")
        o = end_date.split("/")
        p = o[0]
        if str(end_date) < str(start_date):
            print("this reservation isnt possible")
            answer3 = input("would you like to change the dates? ")
            if answer3 == "yes" or answer3 == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
            if int(p) > n:
                print("our policy allows advance reservation upto only 2 years")
                answer2 = input("would you like to change the dates? ")
                if answer2 == "yes" or answer2 == "y":
                    rent_a_car(x, city, user_id)
                else:
                    print("thank you for using the system")
                    exit()
        else:
            if car_type == "manual":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_m where car_type='manual'")
                rs = my_cursor.fetchall()
                if not rs:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city, start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_m(car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"
                    values = [(choice, user_id, start_date, end_date)]
                    my_cursor.executemany(sql_form, values)
                    my_db_m.commit()
                    terms1 = input("Would you like to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city,start_date,end_date,choice)
                    print("thank you for choosing crossroads!")
                    ans2 = input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            elif car_type == "automatic":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_m where car_type='automatic'")  # print price as well
                rs = my_cursor.fetchall()
                if not rs:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city, start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_m(car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"
                    val2 = [(choice, user_id, start_date, end_date)]
                    my_cursor.executemany(sql_form, val2)
                    my_db_m.commit()
                    terms1 = input("Do you want to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city, start_date, end_date, choice)
                    print("thank you for choosing crossroads!")
                    ans2 = input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            else:
                print("please enter one of the given options")
                rent_a_car(x, city, user_id)
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        car_type = input("enter the type of car you prefer(automatic/manual): ")
        start_date = input("enter start date(yyyy/mm/dd): ")
        cur_date = str(datetime.date.today())
        m = cur_date.split("-")
        n = int(m[0]) + 2
        if str(start_date) < str(cur_date):
            print("reservation not possible because of incorrect dates")
            answer = input("enter would you like to change the dates? ")
            if answer == "yes" or answer == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
        else:
            pass
        end_date = input("enter end date(yyyy/mm/dd): ")
        address = input("enter pickup point: ")
        time = input("enter pickup time: ")
        o = end_date.split("/")
        p = o[0]
        if str(end_date) < str(start_date):
            print("this reservation isnt possible")
            answer3 = input("would you like to change the dates? ")
            if answer3 == "yes" or answer3 == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
            if int(p) > n:
                print("our policy allows advance reservation upto only 2 years")
                answer2 = input("would you like to change the dates? ")
                if answer2 == "yes" or answer2 == "y":
                    rent_a_car(x, city, user_id)
                else:
                    print("thanks for using the system")
                    exit()
        else:
            if car_type == "manual":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_l where car_type='manual'")
                rs = my_cursor.fetchall()
                if not rs:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city, start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_l (car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"  # add price
                    values = [(choice, user_id, start_date, end_date)]
                    my_cursor.executemany(sql_form, values)
                    my_db_l.commit()
                    terms1 = input("Do you want to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city, start_date, end_date, choice)
                    print("thank you for choosing crossroads!")
                    ans2 = input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            elif car_type == "automatic":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_l where car_type='automatic'")  # print price as well
                rs = my_cursor.fetchall()
                if not rs:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city, start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_l(car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"
                    val2 = [(choice, user_id, start_date, end_date)]
                    my_cursor.executemany(sql_form, val2)
                    my_db_l.commit()
                    terms1 = input("Do you want to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city, start_date, end_date, choice)
                    print("thank you for choosing crossroads!")
                    ans2 = input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            else:
                print("please enter one of the given options")
                rent_a_car(x, city, user_id)
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
        car_type = input("enter the type of car you prefer(automatic/manual): ")
        start_date = input("enter start date(yyyy/mm/dd): ")
        cur_date = str(datetime.date.today())
        m = cur_date.split("-")
        n = int(m[0]) + 2
        if str(start_date) < str(cur_date):
            print("reservation not possible because of incorrect dates")
            answer = input("enter would you like to change the dates? ")
            if answer == "yes" or answer == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
        else:
            pass
        end_date = input("enter end date(yyyy/mm/dd): ")
        address = input("enter pickup point: ")
        time = input("enter pickup time: ")
        o = end_date.split("/")
        p = o[0]
        if str(end_date) < str(start_date):
            print("this reservation is not possible")
            answer3 = input("would you like to change the dates? ")
            if answer3 == "yes" or answer3 == "y":
                rent_a_car(x, city, user_id)
            else:
                print("thank you for using our system")
                exit()
            if int(p) > n:
                print("our policy allows advance reservation upto only 2 years")
                answer2 = input("would you like to change the dates? ")
                if answer2 == "yes" or answer2 == "y":
                    rent_a_car(x, city, user_id)
                else:
                    print("thanks for using the system")
                    exit()
        else:
            if car_type == "manual":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_p where car_type='manual'")        #print price as well
                rs = my_cursor.fetchall()
                if not rs:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city,start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")                  # enter start_date and end_date again
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_p(car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"
                    values = [(choice,user_id,start_date,end_date)]
                    my_cursor.executemany(sql_form, values)
                    my_db_p.commit()
                    terms1 = input("Do you want to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city, start_date, end_date, choice)
                    print("thank you for choosing crossroads!")
                    ans2 = input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            elif car_type == "automatic":
                my_cursor.execute("select car_id,car_company,car_model from car_inventory_p where car_type='automatic'")     #print price as well
                rs = my_cursor.fetchall()
                if rs == []:
                    print("a car to your specifications is unavailable")
                    ans1 = input("would you like to change the specifications of your car?")
                    if ans1 == "yes" or ans1 == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our system")
                        exit()
                else:
                    print("following cars are available")
                    print("car id     car company      car model")
                    for element in rs:
                        print(element)
                choice = input("enter the car id of the car you wish to rent: ")
                if calendar_fn.calendar(city,start_date, end_date, choice) == False:
                    print("car of choice is not available for selected duration")
                    answer = input("would you like to change the dates or type of your car? ")                  # enter start_date and end_date again
                    if answer == "yes" or answer == "y":
                        rent_a_car(x, city, user_id)
                    else:
                        print("thank you for using our agency")
                        exit()
                else:
                    sql_form = "insert into reservation_p(car_id,user_id,start_time,end_time) values(%s,%s,%s,%s)"
                    val2 = [(choice, user_id, start_date, end_date)]
                    my_cursor.executemany(sql_form, val2)
                    my_db_p.commit()
                    terms1 = input("Do you want to know the Terms and Conditions of renting a car(y/n):")
                    if terms1 == 'y':
                        f1 = open("tandc2.txt", "r")
                        print(f1.read())
                        print()
                        f1.close()
                    print("your reservation has been made. your car will arrive on ", address, " at ", time)
                    billing_fn.billing(city, start_date, end_date, choice)
                    print("thank you for choosing crossroads!")
                    ans2= input("would you like to go back to the home page? ")
                    if ans2 == "y" or ans2 == "yes":
                        choice_fn.choice(city)
                    else:
                        exit()
            else:
                print("please enter one of the given options")
                rent_a_car(x, city, user_id)
