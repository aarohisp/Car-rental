import mysql.connector
import random
from crossroads import rent_out_car
from crossroads import rent_car
from crossroads import cancel_function


def create_password(x,city):
    global user_type
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
    if int(x) == 1:
        user_type = "user"
    elif int(x) == 2:
        user_type = "lender"
    elif int(x) == 3:
        print("there are no reservations in your name")
        inp=input("would you like to login again(y/n)? ")
        if inp == "y" or inp == "yes":
            check_password(x,city)
        else:
            print("thank you for using our system!")
            exit()
    else:
        print("please enter a registered option")
    first_name = input("enter your first name: ")
    last_name = input("enter your last name: ")
    user_name = input("enter a username: ")
    password = input("enter your new password: ")
    user_id = first_name[:2] + last_name[:2] + str(random.randint(100, 999))
    if city == "mumbai":
        sql_form = "insert into user_details_m(user_id,first_name,last_name,password,user_name,user_type) values (%s," \
                   "%s,%s,%s,%s,%s) "
        values = [(user_id, first_name, last_name, password, user_name, user_type)]
        my_cursor.executemany(sql_form, values)
        my_db_m.commit()
        if int(x) == 2:
            rent_out_car.rent_out_a_car(x, city)
        elif int(x) == 1:
            rent_car.rent_a_car(x, city, user_id)
        elif int(x) == 3:
            cancel_function.cancel_res(x,city, user_id)
        else:
            pass
    elif city == "lonavla":
        sql_form = "insert into user_details_l(user_id,first_name,last_name,password,user_name,user_type) values (%s," \
                   "%s,%s,%s,%s,%s) "
        values = [(user_id, first_name, last_name, password, user_name, user_type)]
        my_cursor.executemany(sql_form, values)
        my_db_l.commit()
        if int(x) == 2:
            rent_out_car.rent_out_a_car(x,city)
        elif int(x) == 1:
            rent_car.rent_a_car(x, city, user_id)
        elif int(x) == 3:
            cancel_function.cancel_res(x, city, user_id)
        else:
            pass
    else:
        sql_form = "insert into user_details_p(user_id,first_name,last_name,password,user_name,user_type) values (%s," \
                   "%s,%s,%s,%s,%s) "
        values = [(user_id, first_name, last_name, password, user_name,user_type)]
        my_cursor.executemany(sql_form, values)
        my_db_p.commit()
        if int(x) == 2:
            rent_out_car.rent_out_a_car(x, city)
        elif int(x) == 1:
            rent_car.rent_a_car(x, city,user_id)
        elif int(x) == 3:
            cancel_function.cancel_res(x, city,user_id)
        else:
            pass


def check_password(x,city):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
    user_name = input("enter your username: ")
    password = input("enter your password: ")
    list1 = []
    if city == "mumbai":
        pass2 = "select user_name from user_details_m"
        my_cursor.execute(pass2)
        for element in my_cursor:
            for item in element:
                list1.append(item)
        if user_name not in list1:
            print("please enter correct username and password")
            check_password(x,city)
        else:
            pass1 = "select password from user_details_m where user_name=%s"
            val = [user_name]
            my_cursor.execute(pass1, val)
            for l in my_cursor:
                y = l
                for element in y:
                    m = element
                    if password == m:
                        pass2 = "select first_name from user_details_m where user_name=%s"
                        my_cursor.execute(pass2, val)
                        for n in my_cursor:
                            o = n
                            for p in o:
                                r = p
                                print("welcome ", r)
                        pass3 = "select user_id from user_details_m where user_name=%s"
                        my_cursor.execute(pass3, val)
                        for a in my_cursor:
                            b = a
                            for c in b:
                                d = c
                                user_id = d
                                if int(x) == 1:
                                    rent_car.rent_a_car(x, city, user_id)
                                elif int(x) == 2:
                                    rent_out_car.rent_out_a_car(x, city)
                                elif int(x) == 3:
                                    cancel_function.cancel_res(x, city, user_id)
                                else:
                                    pass
                    else:
                        choice = input('''incorrect password, please choose 
1.to enter your details again       2.create a new account      3.exit: ''')
                        if int(choice) == 1:
                            check_password(x, city)
                        elif int(choice) == 2:
                            create_password(x, city)
                        elif int(choice) == 3:
                            print("thank you for using our agency.come again soon")
                            break
                        else:
                            print("please enter one of the above options")
                            check_password(x,city)
    elif city == "lonavla":
        pass2 = "select user_name from user_details_l"
        my_cursor.execute(pass2)
        for element in my_cursor:
            for item in element:
                list1.append(item)
        if user_name not in list1:
            print("please enter correct username and password")
            check_password(x, city)
        else:
            pass1 = "select password from user_details_l where user_name=%s"
            val = [user_name]
            my_cursor.execute(pass1, val)
            for l in my_cursor:
                y = l
                for element in y:
                    m = element
                    if password == m:
                        pass2 = "select first_name from user_details_l where user_name=%s"
                        my_cursor.execute(pass2, val)
                        for n in my_cursor:
                            o = n
                            for p in o:
                                r = p
                                print("welcome ", r)
                        pass3 = "select user_id from user_details_l where user_name=%s"
                        my_cursor.execute(pass3, val)
                        for a in my_cursor:
                            b = a
                            for c in b:
                                d = c
                                user_id = d
                                if int(x) == 1:
                                    rent_car.rent_a_car(x, city, user_id)
                                elif int(x) == 2:
                                    rent_out_car.rent_out_a_car(x, city)
                                elif int(x) == 3:
                                    cancel_function.cancel_res(x, city, user_id)
                                else:
                                    pass
                    else:
                        choice = input('''incorrect password, please choose 
        1.to enter your details again       2.create a new account      3.exit: ''')
                        if int(choice) == 1:
                            check_password(x, city)
                        elif int(choice) == 2:
                            create_password(x, city)
                        elif int(choice) == 3:
                            print("thank you for using our agency.come again soon")
                            break
                        else:
                            print("please enter one of the above options")
                            check_password(x, city)
    else:
        pass2 = "select user_name from user_details_p"
        my_cursor.execute(pass2)
        for element in my_cursor:
            for item in element:
                list1.append(item)
        if user_name not in list1:
            print("please enter correct username and password")
            check_password(x, city)
        else:
            pass1 = "select password from user_details_p where user_name=%s"
            val = [user_name]
            my_cursor.execute(pass1, val)
            for l in my_cursor:
                y = l
                for element in y:
                    m = element
                    if password == m:
                        pass2 = "select first_name from user_details_p where user_name=%s"
                        my_cursor.execute(pass2, val)
                        for n in my_cursor:
                            o = n
                            for p in o:
                                r = p
                                print("welcome ", r)
                        pass3 = "select user_id from user_details_p where user_name=%s"
                        my_cursor.execute(pass3, val)
                        for a in my_cursor:
                            b = a
                            for c in b:
                                d = c
                                user_id = d
                                if int(x) == 1:
                                    rent_car.rent_a_car(x, city, user_id)
                                elif int(x) == 2:
                                    rent_out_car.rent_out_a_car(x, city)
                                elif int(x) == 3:
                                    cancel_function.cancel_res(x, city, user_id)
                                else:
                                    pass
                    else:
                        choice = input('''incorrect password, please choose 
        1.to enter your details again       2.create a new account      3.exit: ''')
                        if int(choice) == 1:
                            check_password(x, city)
                        elif int(choice) == 2:
                            create_password(x, city)
                        elif int(choice) == 3:
                            print("thank you for using our agency.come again soon")
                            break
                        else:
                            print("please enter one of the above options")
                            check_password(x, city)

