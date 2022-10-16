import mysql.connector
import random
from crossroads import choice_fn


def rent_out_a_car(x,city):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        try:
            lease_start_date = input("please enter the starting date of lease of your car(yyyy/mm/dd): ")  # lease_start_date = (str(input("please enter the starting date of lease of your car: ")).split("/"))[::-1]  #to enter date put a restricn for more than 2 months
            lease_end_date = input("please enter the ending date of lease of your car(yyyy/mm/dd): ")
            car_type = input("is the car automatic or manual? ")
            car_company = input("please enter the car company: ")
            car_model = input("please enter the car model of your car: ")
            mileage = input("please enter the mileage of your car: ")
            color = input("please enter the colour of your car: ")
            number_plate = input("please enter the number plate of your car: ")
            car_category = input("please enter the car category(Sedan/SUV/Hatchback) of your car: ")
            terms = input("Do you want to know the Terms and Conditions of renting out your car(y/n):")
            if terms == 'y':
                f1 = open("tandc1.txt", "r")
                print(f1.read())
                print()
                f1.close()
            car_id = car_company[:2] + str(random.randint(100, 999))
            sql_form = "insert into car_inventory_m(car_id,car_company,car_model,car_type,mileage,color,number_plate," \
                       "lease_start_date,lease_end_date,car_category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            values = [(car_id, car_company, car_model, car_type, mileage, color, number_plate, lease_start_date,lease_end_date, car_category)]
            my_cursor.executemany(sql_form, values)
            my_db_m.commit()
            print("confirming your order.....")
            print('''changes sucessfully made.
thank you for using our agency!''')
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
        except:
            print("please enter the correct information")
            answer = input("would you like to re-enter information?")
            if answer == "y" or answer == "yes":
                rent_out_a_car(x, city)
            else:
                print("thank you for choosing crossroads!")
                exit()
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        try:
            lease_start_date = input("please enter the starting date of lease of your car(yyyy/mm/dd): ")
            lease_end_date = input("please enter the ending date of lease of your car(yyyy/mm/dd): ")
            car_type = input("is the car automatic or manual? ")
            car_company = input("please enter the car company: ")
            car_model = input("please enter the car model of your car: ")
            mileage = input("please enter the mileage of your car: ")
            color = input("please enter the colour of your car: ")
            number_plate = input("please enter the number plate of your car: ")
            car_category = input("please enter the car category(Sedan/SUV/Hatchback) of your car: ")
            terms = input("Do you want to know the Terms and Conditions of renting out your car(y/n):")
            if terms == 'y':
                f1 = open("tandc1.txt", "r")
                print(f1.read())
                print()
                f1.close()
            car_id = car_company[:2] + str(random.randint(100, 999))
            sql_form = "insert into car_inventory_l(car_id,car_company,car_model,car_type,mileage,color,number_plate," \
                       "lease_start_date,lease_end_date,car_category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            values = [(car_id, car_company, car_model, car_type, mileage, color, number_plate, lease_start_date,lease_end_date, car_category)]
            my_cursor.executemany(sql_form, values)
            my_db_l.commit()
            print("confirming your order.....")
            print('''changes sucessfully made.
thank you for using our agency!''')
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
        except:
            print("please enter the correct information")
            answer = input("would you like to re-enter information?")
            if answer == "y" or answer == "yes":
                choice_fn.choice(city)
            else:
                print("thank you for choosing crossroads!")
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
        try:
            lease_start_date = input("please enter the starting date of lease of your car(yyyy/mm/dd): ")
            lease_end_date = input("please enter the ending date of lease of your car(yyyy/mm/dd): ")
            car_type = input("is the car automatic or manual? ")
            car_company = input("please enter the car company: ")
            car_model = input("please enter the car model of your car: ")
            mileage = input("please enter the mileage of your car: ")
            color = input("please enter the colour of your car: ")
            number_plate = input("please enter the number plate of your car: ")
            car_category = input("please enter the car category(Sedan/SUV/Hatchback) of your car: ")
            terms = input("Do you want to know the Terms and Conditions of renting out your car(y/n):")
            if terms == 'y':
                f1 = open("tandc1.txt", "r")
                print(f1.read())
                print()
                f1.close()
            car_id = car_company[:2] + str(random.randint(100, 999))
            sql_form = "insert into car_inventory_p(car_id,car_company,car_model,car_type,mileage,color,number_plate," \
                       "lease_start_date,lease_end_date,car_category) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            values = [(car_id, car_company, car_model, car_type, mileage, color, number_plate, lease_start_date,
                       lease_end_date, car_category)]
            my_cursor.executemany(sql_form, values)
            my_db_p.commit()
            print("confirming your order.....")
            print('''changes sucessfully made.
thank you for using our agency!''')
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
        except:
            print("please enter the correct information")
            answer = input("would you like to re-enter information?")
            if answer == "y" or answer == "yes":
                rent_out_a_car(x, city)
            else:
                print("thank you for choosing crossroads!")

