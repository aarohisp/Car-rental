import mysql.connector
from crossroads import choice_fn


def cancel_res(x,city,user):
    if city == "mumbai":
        my_db_m = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_mumbai')
        my_cursor = my_db_m.cursor()
        sqlform = 'select * from reservation_m where user_id = %s'
        values = [user]
        my_cursor.execute(sqlform, values)
        rs = my_cursor.fetchall()
        if not rs:
            print("there are no reservations in your name")
            print("thank you for using crossroads!")
        else:
            print()
            print(" car_id     user_id          start_time                  end_time")
            print(rs)
            car_id = input("enter the car_id of the reservation to be deleted: ")
            sqlform1 = 'delete from reservation_m where user_id = "{}" and car_id = "{}"'.format(user, car_id)
            my_cursor.execute(sqlform1)
            print("your reservation has been cancelled")
            print("thank you for using our system!")
            my_db_m.commit()
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
            exit()
    elif city == "lonavla":
        my_db_l = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_lonavla')
        my_cursor = my_db_l.cursor()
        sqlform = 'select * from reservation_l where user_id = %s'
        values = [user]
        my_cursor.execute(sqlform, values)
        rs = my_cursor.fetchall()
        if not rs:
            print("there are no reservations in your name")
            exit()
        else:
            print()
            print(" car_id     user_id          start_time                  end_time")
            print(rs)
            car_id = input("enter the car_id of the reservation to be deleted: ")
            sqlform1 = 'delete from reservation_l where user_id = "{}" and car_id = "{}"'.format(user, car_id)
            my_cursor.execute(sqlform1)
            print("your reservation has been cancelled")
            print("thank you for using our system!")
            my_db_l.commit()
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
            exit()
    else:
        my_db_p = mysql.connector.connect(host="newlap", user="appuser", passwd="pass123",
                                          auth_plugin='mysql_native_password', db='car_project_pune')
        my_cursor = my_db_p.cursor()
        sqlform = 'select * from reservation_p where user_id = %s'
        values = [user]
        my_cursor.execute(sqlform, values)
        rs = my_cursor.fetchall()
        if not rs:
            print("there are no reservations in your name")
            exit()
        else:
            print()
            print(" car_id     user_id          start_time                  end_time")
            print(rs)
            car_id = input("enter the car_id of the reservation to be deleted: ")
            sqlform1 = 'delete from reservation_p where user_id = "{}" and car_id = "{}"'.format(user, car_id)
            my_cursor.execute(sqlform1)
            print("your reservation has been cancelled")
            print("thank you for using our system!")
            my_db_p.commit()
            ans2 = input("would you like to go back to the home page? ")
            if ans2 == "y" or ans2 == "yes":
                choice_fn.choice(city)
            else:
                exit()
            exit()
