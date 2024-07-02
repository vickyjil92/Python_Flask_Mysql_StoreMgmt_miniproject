import datetime
import mysql.connector


__con = None
def get_sql_connection():
    print("Opening mysql connection")
    global __con
    if __con is None:
        __con = mysql.connector.connect(user='root',password='root',
                                              host='127.0.0.1',
                                              database='general_store')

    return __con
