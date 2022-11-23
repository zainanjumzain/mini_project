product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]
shopping_cart = []

print("\nGeneration Cafe\n")

def main_menu():
    while True:
        try:
            print("\nMain Menu Options\n")
            print("0 - Exit Application")
            print("1 - View System Menu\n")
            first_option = int(input("Enter a number: "))
            if first_option == 0:
                print("\nApplication Exited\n")
                exit()
            elif first_option == 1:
                product_menu()
            else:
                print("\nSelection not available. Please select 0 or 1.")
                main_menu()
                break
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.")
                
def product_menu():
    while True:
        try:
            print("\nSystem Menu\n")
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
                    print(f"'{empty_shopping_cart}' Not in Product List")
            elif second_option == 3:
                print("\nRemove item from Shopping Cart\n")
                new_updated_shopping_cart = str(input("What items would you like to remove? ")).title()
                if new_updated_shopping_cart in product_list:
                    shopping_cart.remove(new_updated_shopping_cart)
                    print("\nShopping Cart:", shopping_cart)
                else:
                    print(f"'{new_updated_shopping_cart}' Not in Shopping Cart")
            elif second_option == 4:
                print("\nFinal Shopping Cart:", shopping_cart, "\n")
                print("Order Details")
                break
            else:
                print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and product_menu()

main_menu()

# print("\nQ2\n")
# car["model"] = "Focus"
# print("modified", car)
# 
# print("\nQ3\n")
# del car["model"]
# print("del", car)