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

products = []
shopping_cart = []
cursor = connection.cursor()
cursor.execute('SELECT * FROM Products_Table')
rows = cursor.fetchall()
for row in rows:
    products.append(f'{str(row[0])}')
cursor.close()


cursor = connection.cursor()
cursor.execute('SELECT * FROM Couriers_Table')
rows = cursor.fetchall()
for row in rows:
    print(f'{str(row[0])}')
cursor.close()
connection.close()

print(products)

empty_shopping_cart = str(input("What items would you like to add? ")).title()
if empty_shopping_cart in products:
    os.system('cls')
    shopping_cart.append(empty_shopping_cart)
    print("\nShopping Cart:", shopping_cart)
else:
    os.system('cls')
    print("\n",f"'{empty_shopping_cart}' Not in Product List")