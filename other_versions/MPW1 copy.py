product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]

print("Main Menu Options")
shopping_cart = []
print("0 - Exit Application")
print("1 - View System Menu")
while True:
    first_option = int(input("Enter a number: "))
    if first_option == 0:
        print("Application Exited")
        exit()
    elif first_option == 1:
        print("Product Menu")
        print("0 - Exit Application")
        print("1 - View Product List")
        print("2 - Add Item to Shopping Cart")
        print("3 - Remove Item from Shopping Cart")
        print("4 - View Final Shopping Cart")
        while True:
            second_option = int(input("Enter a number: "))
            if second_option == 0:
                print("Application Exited")
            while True:
                if second_option == 1:
                    print("Product List:", product_list)
                elif second_option == 2:
                    print("Shopping Cart")
                    empty_shopping_cart = str(input("What items would you like to add? "))
                    shopping_cart.append(empty_shopping_cart)
                    print("Shopping Cart:", shopping_cart)
                elif second_option == 3:
                    print("Updated Shopping Cart")
                    new_updated_shopping_cart = str(input("What items would you like to remove? "))
                    shopping_cart.remove(new_updated_shopping_cart)
                    print("Shopping Cart:", shopping_cart)
                elif second_option == 4:
                    print("Final Shopping Cart")
                    print("Shopping Cart:", shopping_cart)
                    exit()  
