

from turtle import clear


product_list = ["Still Water", "Sparking Water", "Coke", "Sprite", "Fanta", "Diet Coke", "Apple Juice"]

print("Main Menu Options")

first_option = int(input("Enter 1 for Product Menu or 0 to exit: "))
if first_option == 0:
    print("Application Exited")
    exit()
elif first_option == 1:
    print("Product Menu")

second_option = (int(input("Enter 1 to view Product List or press 0 to return to Main Menu: ")))
if second_option == 0:
    print("Returned to Main Menu Options")
    
elif second_option == 1:
    print("Product List:", product_list)

shopping_cart = []

third_option = (int(input("Enter 1 to create a Shopping Cart and add items or press 0 to return to Main Menu: ")))
if third_option == 0:
    print("Returned to Main Menu Options")
elif third_option == 1:
    print("Shopping Cart")
    empty_shopping_cart = str(input("What items would you like to add? "))
    shopping_cart.append(empty_shopping_cart)
    print("Shopping Cart:", shopping_cart)


fourth_option = (int(input("Enter 1 to add more to Shopping Cart or press 0 to return to Main Menu: ")))
if fourth_option == 0:
    print("Returned to Main Menu Options")
elif fourth_option == 1:
    print("Updated Shopping Cart")
    updated_shopping_cart = str(input("What items would you like to add? "))
    shopping_cart.append(updated_shopping_cart)
    print("Shopping Cart:", shopping_cart)


fifth_option = (int(input("Enter 1 to delete item or press 0 to return to Main Menu: ")))
if fifth_option == 0:
    print("Returned to Main Menu Options")
elif fifth_option == 1:
    print("Updated Shopping Cart")
    new_updated_shopping_cart = str(input("What items would you like to remove? "))
    shopping_cart.remove(new_updated_shopping_cart)
    print("Shopping Cart:", shopping_cart)
