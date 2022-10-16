import mysql.connector
from crossroads import choice_fn

print("welcome to crossroads!")

city = input("enter the city you wish to conduct your business in (pune/lonavla/mumbai): ")
if city == "mumbai":
    pass
elif city == "lonavla":
    pass
elif city == "pune":
    pass
else:
    print("please choose between the given cities")
    city = input("enter the city you wish to rent/lend your car in (pune/lonavla/mumbai): ")
global x


def remove_exp(city):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        my_cursor.execute("select car_id from car_inventory_m where lease_end_date < curdate()")  # print price as well
        rs = my_cursor.fetchall()
        for item in rs:
            sqlform2 = "delete from reservation_m where car_id =%s"
            my_cursor.execute(sqlform2, item)
            sqlform3 = "delete from car_inventory_m where car_id =%s"
            my_cursor.execute(sqlform3, item)
        print("Expired cars reservation entries removed ....")
        print("Expired cars entries removed from Car inventory....")
        my_db_m.commit()
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        my_cursor.execute("select car_id from car_inventory_l where lease_end_date < curdate()")  # print price as well
        rs = my_cursor.fetchall()
        for item in rs:
            sqlform2 = "delete from reservation_l where car_id =%s"
            my_cursor.execute(sqlform2, item)
            sqlform3 = "delete from car_inventory_l where car_id =%s"
            my_cursor.execute(sqlform3, item)
        print("Expired cars reservation entries removed ....")
        print("Expired cars entries removed from Car inventory....")
        my_db_l.commit()
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
        my_cursor.execute("select car_id from car_inventory_p where lease_end_date < curdate()")  # print price as well
        rs = my_cursor.fetchall()
        for item in rs:
            sqlform2 = "delete from reservation_p where car_id =%s"
            my_cursor.execute(sqlform2, item)
            sqlform3 = "delete from car_inventory_p where car_id =%s"
            my_cursor.execute(sqlform3, item)
        print("Expired cars reservation entries removed ....")
        print("Expired cars entries removed from Car inventory....")
        my_db_p.commit()


remove_exp(city)

choice_fn.choice(city)
