# Notes
# Have an option to in the main_menu() to view previous orders by pulling it from an order file
# Have product_list and list_of_couriers in a differnt file that you need to pull in
# At the end of the order, persist the order to a order file to you can do previous order step
# at the end of the order also have thank you message and return to main menu right after or be able to exit
# First time coding so this is ok but need more practise
import csv
import datetime
import os
os.system('cls')

product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]
list_of_couriers = ["Uber Eats", "Deliveroo", "Just Eat", "Food Panda", "Gopuff"]
courier_list = {
    'Courier Name': "Not Providied"
}
shopping_cart = []
order_details = {
    'Customer Name': "Not Providied",
    'Customer Address': "Not Providied",
    'Customer Phone Number': "Not Providied",
    'Status of Order': "Preparing"
}
orders = []
courier = []
print("\Welcome To Dave's Cafe\n")

def main_menu():
    while True:
        try:
            print("\nMain Menu Options\n")
            print("0 - Exit Application")
            print("1 - View Product Menu\n")
            first_option = int(input("Enter a number: "))
            if first_option == 0:
                print("\nApplication Exited\n")
                exit()
            elif first_option == 1:
                os.system('cls')
                product_menu()
            else:
                os.system('cls')
                print("\nSelection not available. Please select 0 or 1.")
                main_menu()
        except Exception as e:
            os.system('cls')
            print("\nSelection not available. Please select a vaild number.")

def product_menu():
    while True:
        try:
            print("\nProduct Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - View Product List")
            print("2 - Add Item to Shopping Cart")
            print("3 - Remove Item from Shopping Cart")
            print("4 - View Final Shopping Cart\n")
            second_option = int(input("Enter a number: "))
            if second_option == 0:
                os.system('cls')
                print("\nBack to Main Menu\n")
                main_menu()
            elif second_option == 1:
                os.system('cls')
                print("\nProduct List:", product_list)
            elif second_option == 2:
                os.system('cls')
                print("\nAdd item to Shopping Cart\n")
                empty_shopping_cart = str(input("What items would you like to add? ")).title()
                if empty_shopping_cart in product_list:
                    os.system('cls')
                    shopping_cart.append(empty_shopping_cart)
                    print("\nShopping Cart:", shopping_cart)
                else:
                    os.system('cls')
                    print("\n",f"'{empty_shopping_cart}' Not in Product List")
            elif second_option == 3:
                os.system('cls')
                print("\nRemove item from Shopping Cart\n")
                new_updated_shopping_cart = str(input("What items would you like to remove? ")).title()
                if new_updated_shopping_cart in product_list:
                    os.system('cls')
                    shopping_cart.remove(new_updated_shopping_cart)
                    print("\nShopping Cart:", shopping_cart)
                else:
                    os.system('cls')
                    print("\n",f"'{new_updated_shopping_cart}' Not in Shopping Cart")
            elif second_option == 4:
                os.system('cls')
                print("\nFinal Shopping Cart:", shopping_cart, "\n")
                print("\nCourier Menu\n")
                courier_menu()
            else:
                os.system('cls')
                print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
        except Exception as e:
            os.system('cls')
            print("\nSelection not available. Please select a vaild number.") and product_menu()

def courier_menu():
    while True:
        try:
            print("\nCourier Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product Menu")
            print("2 - Add or Change Courier")
            print("3 - View current Courier")
            print("4 - Go to Order Menu\n")
            courier_option = int(input("Enter a number: "))
            if courier_option == 0:
                os.system('cls')
                print("\nBack to Main Menu\n")
                main_menu()
            elif courier_option == 1:
                os.system('cls')
                print("\nBack to Product Menu\n")
                product_menu()
            elif courier_option == 2:
                os.system('cls')
                print("\nCourier Options\n")
                print("\nCourier List:", list_of_couriers)
                select_courier = str(input("\nWhich Courier would you like? ")).title()
                if select_courier in list_of_couriers:
                    os.system('cls')
                    courier_list["Courier Name"] = f"{select_courier}"
                else:
                    os.system('cls')
                    print("\n",f"'{select_courier}' Not a valid Courier")
            elif courier_option == 3:
                os.system('cls')
                for key, value in courier_list.items():
                    print("\n", key, ":", value)    
            elif courier_option == 4:
                os.system('cls')
                print("\nOrder Menu\n")
                order_menu()
            else:
                os.system('cls')
                print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
        except Exception as e:
            os.system('cls')
            print("\nSelection not available. Please select a vaild number.") and courier_menu()

def order_menu():
    while True:
        try:
            print("\nOrder Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product Menu")
            print("2 - Go back to Courier Menu")
            print("3 - Add or Change Customer Details") 
            print("4 - Go to Order Status Menu\n")
            third_option = int(input("Enter a number: "))
            if third_option == 0:
                os.system('cls')
                print("\nBack to Main Menu\n")
                main_menu()
            elif third_option == 1:
                os.system('cls')
                print("\nBack to Product Menu\n")
                product_menu()
            elif third_option == 2:
                os.system('cls')
                print("\nBack to Courier Menu\n")
                courier_menu()
            elif third_option == 3:
                os.system('cls')
                while True:
                    try:
                        print("\nCustomer Details\n")
                        print("0 - Go back to Order Menu")
                        print("1 - Add or Change Customer Name")
                        print("2 - Add or Change Customer Address")
                        print("3 - Add or Change Customer Phone Number")
                        print("4 - View Customer Details\n")
                        customer_option = int(input("Enter a number: "))
                        if customer_option == 0:
                            os.system('cls')
                            print("\nBack to Order Menu\n")
                            order_menu()
                        elif customer_option == 1:
                            os.system('cls')
                            customer_name = str(input("\nWhat is the customers name? ")).title()
                            order_details["Customer Name"] = f"{customer_name}"
                        elif customer_option == 2:
                            os.system('cls')
                            customer_address = str(input("\nWhat is the customers address? ")).title()
                            order_details["Customer Address"] = f"{customer_address}"
                        elif customer_option == 3:
                            os.system('cls')
                            customer_phone_number = str(input("\nWhat is the customers phone number? "))
                            order_details["Customer Phone Number"] = f"{customer_phone_number}"
                        elif customer_option == 4:
                            os.system('cls')
                            for key, value in order_details.items():
                                print("\n", key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                            for key, value in courier_list.items():
                                print("\n", key, ":", value)   
                        else:
                            os.system('cls')
                            print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
                    except Exception as e:
                        print("\nSelection not available. Please select a vaild number.")
            elif third_option == 4:
                os.system('cls')
                print("\nOrder Status Menu\n")
                order_status()
            else:
                os.system('cls')
                print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and order_menu()
                 
def order_status():
    while True:
        try:
            print("\nOrder Status Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product Menu")
            print("2 - Go back to Courier Menu")
            print("3 - Go back To Order Menu")
            print("4 - Update Order Status")
            print("5 - View all Orders\n")
            fourth_option = int(input("Enter a number: "))
            if fourth_option == 0:
                os.system('cls')
                print("\nBack to Main Menu\n")
                main_menu()
            elif fourth_option == 1:
                os.system('cls')
                print("\nBack to Product Menu\n")
                product_menu()
            elif fourth_option == 2:
                os.system('cls')
                print("\nBack to Courier Menu\n")
                courier_menu()               
            elif fourth_option == 3:
                os.system('cls')
                print("\nBack To Order Menu\n")
                order_menu()
            elif fourth_option == 4:
                os.system('cls')
                while True:
                    try:
                        print("\nUpdate Order Status\n")
                        print("0 - Go back to Order Status Menu")
                        print("1 - Change Order Status to Preparing")
                        print("2 - Change Order Status to Ready")
                        print("3 - Change Order Status to Out For Delivery")
                        print("4 - Change Order Status to Delivered\n")
                        status_of_order = int(input("Enter a number: "))
                        if status_of_order == 0:
                            os.system('cls')
                            print("\nBack to Order Status Menu\n")
                            order_status()
                        elif status_of_order == 1:
                            os.system('cls')
                            order_details["Status of Order"] = "Preparing"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                            for key, value in courier_list.items():
                                print("\n", key, ":", value) 
                        elif status_of_order == 2:
                            os.system('cls')
                            order_details["Status of Order"] = "Ready"
                            for key, value in order_details.items():
                                os.system('cls')
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                            for key, value in courier_list.items():
                                os.system('cls')
                                print("\n", key, ":", value) 
                        elif status_of_order == 3:
                            os.system('cls')
                            order_details["Status of Order"] = "Out For Delivery"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                            for key, value in courier_list.items():
                                print("\n", key, ":", value) 
                        elif status_of_order == 4:
                            os.system('cls')
                            order_details["Status of Order"] = "Delivered"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                            for key, value in courier_list.items():
                                print("\n", key, ":", value) 
                        else:
                            os.system('cls')
                            print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
                    except Exception as e:
                        os.system('cls')
                        print("\nSelection not available. Please select a vaild number.")        
            elif fourth_option == 5:
                os.system('cls')
                order_details["Final Shopping Card"] = shopping_cart
                courier.append(courier_list)
                orders.append(order_details)
                orders.append(courier_list)
                print("\nAll Orders: ", orders)
            else:
                os.system('cls')
                print("\nSelection not available. Please select 0, 1, 2, 3, 4 or 5.")
        except Exception as e:
            os.system('cls')
            print("\nSelection not available. Please select a vaild number.") and order_status()
main_menu()