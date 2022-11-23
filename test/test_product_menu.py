from unittest.mock import patch

def product_menu():
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
        elif second_option == 1:
            print("Product List\n")
        elif second_option == 2:
            print("\nAdd item to Shopping Cart\n")
        elif second_option == 3:
            print("\nRemove item from Shopping Cart\n")
        elif second_option == 4:
            print("\nCourier Menu\n")
        else:
            print("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
    except Exception as e:
        print("\nSelection not available. Please select a vaild number.") and product_menu()

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu1(mock_print, mock_input):
    mock_input.return_value = 0
    product_menu()
    mock_print.assert_called_with("\nBack to Main Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu2(mock_print, mock_input):
    mock_input.return_value = 1
    product_menu()
    mock_print.assert_called_with("Product List\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu3(mock_print, mock_input):
    mock_input.return_value = 2
    product_menu()
    mock_print.assert_called_with("\nAdd item to Shopping Cart\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu4(mock_print, mock_input):
    mock_input.return_value = 3
    product_menu()
    mock_print.assert_called_with("\nRemove item from Shopping Cart\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu5(mock_print, mock_input):
    mock_input.return_value = 4
    product_menu()
    mock_print.assert_called_with("\nCourier Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu6(mock_print, mock_input):
    mock_input.return_value = 5
    product_menu()
    mock_print.assert_called_with("\nSelection not available. Please select 0, 1, 2, 3, or 4.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_product_menu7(mock_print, mock_input):
    mock_input.return_value = str()
    product_menu()
    mock_print.assert_called_with("\nSelection not available. Please select a vaild number.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7