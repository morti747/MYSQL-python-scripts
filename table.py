import mysql.connector as mysql
from mysql.connector import Error

host = "10.13.237.100"
user = 'morty'
password = "Password123@$"

try:
    db = mysql.connect(host=host, user=user, password=password)
    print("Connected successfully")
except Exception as e:
    print(e)
    print("Failed to connect")


# Creating a database 

try:
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE IF NOT EXISTS MORTIMAINTENANCE;")
    print("MORTIMAINTENANCE has been created ")

except Exception as e:
    print(e)
    print("Failed to connect")




try:
    command_handler = db.cursor()
    command_handler.execute("USE MORTIMAINTENANCE ;")

    command_handler.execute("CREATE TABLE IF NOT EXISTS Clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(100), email VARCHAR(100))")
    print ("Table Clients has been created successfully ")

    command_handler.execute("CREATE TABLE IF NOT EXISTS Orders (id INT AUTO_INCREMENT PRIMARY KEY, client VARCHAR(100), date_recepetion VARCHAR(100), price VARCHAR(100))")
    print ("Table Orders has been created successfully ")

    command_handler.execute("SHOW TABLES ;")
    print ("Showing all tables in the databases")
    for table in command_handler:
        print(table)



except Exception as e:
    print("Table could not be created ")
    print(e)



finally:
    if db.is_connected():
        command_handler.close()
        db.close()
        print("MySQL connection is closed")






