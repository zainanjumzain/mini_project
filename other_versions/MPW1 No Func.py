product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]
shopping_cart = []

print("\nGeneration Drinks\n")

while True:
    print("\nMain Menu Options\n")
    print("0 - Exit Application")
    print("1 - View System Menu\n")
    try:
        first_option = int(input("Enter a number: "))
        if first_option == 0:
            print("\nApplication Exited\n")
            exit()
        elif first_option == 1:
            while True:
                print("\nSystem Menu\n")
                print("0 - Exit Application")
                print("1 - View Product List")
                print("2 - Add Item to Shopping Cart")
                print("3 - Remove Item from Shopping Cart")
                print("4 - View Final Shopping Cart\n")
                second_option = int(input("Enter a number: "))
                if second_option == 0:
                    print("\nApplication Exited\n")
                    exit()
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
                    exit()
                else:
                    print("\nSelection not available. Please select 0, 1, 2, 3, or 4. Sending back to System Menu.")
        else:
            print("\nSelection not available. Please select 0 or 1. Sending back to Main Menu.")
    except Exception as e:
        print("\nSelection not available. Please select a vaild number. Sending back to Main Menu.")
