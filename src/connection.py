import mysql.connector
import time

import connection

""" # Connect to MySQL
conn = connection.connect("database","sys","root","test")

# Disconnect from MySQL
if conn is not None:
    connection.disconnect(conn)
else:
    print("Flask startup aborted")
    exit
 """

from mysql.connector import Error


def connect(db_host, db_name, db_user, db_pwd):
    for x in range(5):
        print("Attempting to connect...")   
        try:
            connection = mysql.connector.connect(host=db_host,
                                                database=db_name,
                                                user=db_user,
                                                password=db_pwd)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Your connected to database: ", record)
                return connection
        except Error as e:
            print("Error while connecting to MySQL", e)
        
        time.sleep(5)


def disconnect(connection):
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
    else:
        print("Not connected to the database")