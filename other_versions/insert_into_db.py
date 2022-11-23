import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host,
    user,
    password,
    database
)

cursor = connection.cursor()

# cursor.execute("INSERT INTO person(first_name, last_name, age) VALUES('Aleeza', 'Ali', 17)")
connection.commit()
cursor.close()
connection.close()

# Mini project 

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

cursor = connection.cursor()
cursor.execute("INSERT INTO Orders_Table(CustomerName, CustomerAddress, CustomerPhoneNumber, OrderStatus, FinalOrder, CourierName, OrderDateTime) VALUES(f'{CustomerName}', '{CustomerAddress}', '{CustomerPhoneNumber}', '{OrderStatus}', '{FinalOrder}', '{CourierName}', '{OrderDateTime}')")
connection.commit()
cursor.close()
connection.close()