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
cursor.execute('SELECT * FROM Products_Table')
rows = cursor.fetchall()
for row in rows:
    print(f'{str(row[0])}')
cursor.close()


cursor = connection.cursor()
cursor.execute('SELECT * FROM Couriers_Table')
rows = cursor.fetchall()
for row in rows:
    print(f'{str(row[0])}')
cursor.close()
connection.close()