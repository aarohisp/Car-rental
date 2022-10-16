import mysql.connector
import datetime


def calendar(city, date_i, date_f, c_id):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        sql_form = "select lease_start_date,lease_end_date from car_inventory_m where car_id=%s"
        val1 = [c_id]
        my_cursor.execute(sql_form, val1)
        print()
        for element in my_cursor:
            lease_start = element[0]
            lease_end = element[1]
            dti = datetime.datetime.strptime(date_i, '%Y/%m/%d')
            dtf = datetime.datetime.strptime(date_f, '%Y/%m/%d')
            dtid = dti.date()
            dtfd = dtf.date()
            if dtid > lease_start and dtid < lease_end and dtfd > lease_start and dtfd < lease_end:
                return True
            else:
                print(
                    "for the available car the given details are invalid,please enter appropriate dates for leasing of the car")
                return False
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        sql_form = "select lease_start_date,lease_end_date from car_inventory_l where car_id=%s"
        val1 = [c_id]
        my_cursor.execute(sql_form, val1)
        print()
        for element in my_cursor:
            lease_start = element[0]
            lease_end = element[1]
            dti = datetime.datetime.strptime(date_i, '%Y/%m/%d')
            dtf = datetime.datetime.strptime(date_f, '%Y/%m/%d')
            dtid = dti.date()
            dtfd = dtf.date()
            if dtid > lease_start and dtid < lease_end and dtfd > lease_start and dtfd < lease_end:
                return True
            else:
                print(
                    "for the available car the given details are invalid,please enter appropriate dates for leasing of the car")
                return False
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune ')
        my_cursor = my_db_p.cursor()
        sql_form = "select lease_start_date,lease_end_date from car_inventory_p where car_id=%s"
        val1 = [c_id]
        my_cursor.execute(sql_form, val1)
        print()
        for element in my_cursor:
            lease_start = element[0]
            lease_end = element[1]
            dti = datetime.datetime.strptime(date_i, '%Y/%m/%d')
            dtf = datetime.datetime.strptime(date_f, '%Y/%m/%d')
            dtid = dti.date()
            dtfd = dtf.date()
            if dtid > lease_start and dtid < lease_end and dtfd > lease_start and dtfd < lease_end:
                return True
            else:
                print(
                    "for the available car the given details are invalid,please enter appropriate dates for leasing of the car")
                return False
