product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]
shopping_cart = []
order_details = {
    'Customer Name': "Not Providied",
    'Customer Address': "Not Providied",
    'Customer Phone Number': "Not Providied",
    'Status of Order': "Preparing"
}
orders = []
print("\nGeneration Cafe\n")

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
                product_menu()
            else:
                print("\nSelection not available. Please select 0 or 1.")
                main_menu()
        except Exception as e:
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
                print("\nBack to Main Menu\n")
                main_menu()
            elif second_option == 1:
                print("\nProduct List:", product_list)
            elif second_option == 2:
                print("\nAdd item to Shopping Cart\n")
                empty_shopping_cart = str(input("What items would you like to add? ")).title()
                if empty_shopping_cart in product_list:
                    shopping_cart.append(empty_shopping_cart)
                    print("\nShopping Cart:", shopping_cart)
                else:
                    print("\n",f"'{empty_shopping_cart}' Not in Product List")
            elif second_option == 3:
                print("\nRemove item from Shopping Cart\n")
                new_updated_shopping_cart = str(input("What items would you like to remove? ")).title()
                if new_updated_shopping_cart in product_list:
                    shopping_cart.remove(new_updated_shopping_cart)
                    print("\nShopping Cart:", shopping_cart)
                else:
                    print("\n",f"'{new_updated_shopping_cart}' Not in Shopping Cart")
            elif second_option == 4:
                print("\nFinal Shopping Cart:", shopping_cart, "\n")
                order_menu()
            else:
                print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and product_menu()

def order_menu():
    while True:
        try:
            print("\nOrder Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product List")
            print("2 - Add or Change Customer Details") # add a 2.1 and 2.2
            print("3 - Go to Order Status Menu\n")
            third_option = int(input("Enter a number: "))
            if third_option == 0:
                print("\nBack to Main Menu\n")
                main_menu()
            elif third_option == 1:
                print("\nBack to System Menu\n")
                product_menu()
            elif third_option == 2:
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
                            print("\nBack to Order Menu\n")
                            order_menu()
                        elif customer_option == 1:
                            customer_name = str(input("\nWhat is the customers name? ")).title()
                            order_details["Customer Name"] = f"{customer_name}"
                        elif customer_option == 2:
                            customer_address = str(input("\nWhat is the customers address? ")).title()
                            order_details["Customer Address"] = f"{customer_address}"
                        elif customer_option == 3:
                            customer_phone_number = int(input("\nWhat is the customers phone number? 0"))
                            order_details["Customer Phone Number"] = f"{customer_phone_number}"
                        elif customer_option == 4:
                            for key, value in order_details.items():
                                print("\n", key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                        else:
                            print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
                    except Exception as e:
                        print("\nSelection not available. Please select a vaild number.")
            elif third_option == 3:
                print("\nOrder Status Menu\n")
                order_status()
            else:
                print("\nSelection not available. Please select 0, 1, 2 or 3.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and order_menu()
                 
def order_status():
    while True:
        try:
            print("\nOrder Status Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product List")
            print("2 - Go back To Order Menu")
            print("3 - Update Order Status")
            print("4 - View all Orders\n")
            fourth_option = int(input("Enter a number: "))
            if fourth_option == 0:
                print("\nBack to Main Menu\n")
                main_menu()
            elif fourth_option == 1:
                print("\nBack to System Menu\n")
                product_menu()           
            elif fourth_option == 2:
                print("\nBack To Order Menu\n")
                order_menu()
            elif fourth_option == 3:
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
                            print("\nBack to Order Status Menu\n")
                            order_status()
                        elif status_of_order == 1:
                            order_details["Status of Order"] = "Preparing"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                        elif status_of_order == 2:
                            order_details["Status of Order"] = "Ready"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                        elif status_of_order == 3:
                            order_details["Status of Order"] = "Out For Delivery"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                        elif status_of_order == 4:
                            order_details["Status of Order"] = "Delivered"
                            for key, value in order_details.items():
                                print("\n",key, ":", value)
                            print("\n Final Shopping Cart:",shopping_cart)
                        else:
                            print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
                    except Exception as e:
                        print("\nSelection not available. Please select a vaild number.")        
            elif fourth_option == 4:
                order_details["Final Shopping Card"] = shopping_cart
                orders.append(order_details)
                print("\nAll Orders: ", order_details)
            else:
                print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and order_status()
main_menu()