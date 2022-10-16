import mysql.connector
import datetime


def billing(city, st, en, cid):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        dti = datetime.datetime.strptime(st, '%Y/%m/%d')
        dtf = datetime.datetime.strptime(en, '%Y/%m/%d')
        dt_st = dti.date()
        dt_en = dtf.date()
        delta = (dt_en - dt_st)
        sql_form = "select car_category from car_inventory_m where car_id=%s"
        val1 = [cid]
        my_cursor.execute(sql_form, val1)
        for element in my_cursor:
            car_cat = element[0]
            num_of_days = delta.days + 1
            if car_cat == 'Hatchback':
                total_cost = num_of_days * 2000
            elif car_cat == 'Sedan':
                total_cost = num_of_days * 3000
            else:
                total_cost = num_of_days * 5000
            print()
            print("__________________________________________")
            print("                  BILL                    ")
            print("__________________________________________")
            print("    THANK YOU FOR USING CROSSROADS!!      ")
            print("__________________________________________")
            print("")
            print("The total amount you have to pay is Rs.", total_cost)
            print("__________________________________________")
            print()

    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                      auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        dti = datetime.datetime.strptime(st, '%Y/%m/%d')
        dtf = datetime.datetime.strptime(en, '%Y/%m/%d')
        dt_st = dti.date()
        dt_en = dtf.date()
        delta = (dt_en - dt_st)
        sql_form = "select car_category from car_inventory_l where car_id=%s"
        val1 = [cid]
        my_cursor.execute(sql_form, val1)
        for element in my_cursor:
            car_cat = element[0]
            num_of_days = delta.days + 1
            if car_cat == 'Hatchback':
                total_cost = num_of_days * 2000
            elif car_cat == 'Sedan':
                total_cost = num_of_days * 3000
            else:
                total_cost = num_of_days * 5000
            print()
            print("__________________________________________")
            print("                  BILL                    ")
            print("__________________________________________")
            print("    THANK YOU FOR USING CROSSROADS!!      ")
            print("__________________________________________")
            print("")
            print("The total amount you have to pay is Rs.", total_cost)
            print("__________________________________________")
            print()
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                  auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
        dti = datetime.datetime.strptime(st, '%Y/%m/%d')
        dtf = datetime.datetime.strptime(en, '%Y/%m/%d')
        dt_st = dti.date()
        dt_en = dtf.date()
        delta = (dt_en - dt_st)
        sql_form = "select car_category from car_inventory_p where car_id=%s"
        val1 = [cid]
        my_cursor.execute(sql_form, val1)
        for element in my_cursor:
            car_cat = element[0]
            num_of_days = delta.days + 1
            if car_cat == 'Hatchback' or car_cat == "hatchback":
                total_cost = num_of_days * 2000
            elif car_cat == 'Sedan' or car_cat == "sedan":
                total_cost = num_of_days * 3000
            else:
                total_cost = num_of_days * 5000
            print()
            print("__________________________________________")
            print("                  BILL                    ")
            print("__________________________________________")
            print("    THANK YOU FOR USING CROSSROADS!!      ")
            print("__________________________________________")
            print("")
            print("The total amount you have to pay is Rs.", total_cost)
            print("__________________________________________")
            print()