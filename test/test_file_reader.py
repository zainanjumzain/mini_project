from unittest.mock import patch
from dotenv import load_dotenv
import os
import pymysql

products = []
couriers = []

def file_reader():
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
        products.append(f'{str(row[1])}')
        print(products)
    cursor.close()


    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Couriers_Table')
    rows = cursor.fetchall()
    for row in rows:
        couriers.append(f'{str(row[1])}')
        print(couriers)
    cursor.close()
    connection.close()
file_reader()

@patch("builtins.print")
def test_file_reader1(mock_print):
    file_reader()
    mock_print.assert_called_with(['Uber Eats', 'Just Eat', 'Deliveroo', 'Food Panda', 'Gopuff', 'Uber Eats', 'Just Eat', 'Deliveroo', 'Food Panda', 'Gopuff'])
    assert mock_print.call_count == 12

@patch("builtins.print")
def test_file_reader2(mock_print):
    file_reader()
    mock_print.assert_called_with(['Uber Eats', 'Just Eat', 'Deliveroo', 'Food Panda', 'Gopuff', 'Uber Eats', 'Just Eat', 'Deliveroo', 'Food Panda', 'Gopuff', 'Uber Eats', 'Just Eat', 'Deliveroo', 'Food Panda', 'Gopuff'])
    assert mock_print.call_count == 12