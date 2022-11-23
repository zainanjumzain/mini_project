from unittest.mock import patch

def order_menu():
        try:
            print("\nOrder Menu Options\n")
            print("0 - Go back to Main Menu")
            print("1 - Go back to Product Menu")
            print("2 - Go back to Courier Menu")
            print("3 - Add or Change Customer Details") 
            print("4 - Go to Order Status Menu\n")
            third_option = int(input("Enter a number: "))
            if third_option == 0:
                print("\nBack to Main Menu\n")
            elif third_option == 1:
                print("\nBack to Product Menu\n")
            elif third_option == 2:
                print("\nBack to Courier Menu\n")
            elif third_option == 3:
                print("\nCustomer Details\n")
            elif third_option == 4:
                print("\nOrder Status Menu\n")
            else:
                print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
        except Exception as e:
            print("\nSelection not available. Please select a vaild number.") and order_menu()
                 
@patch("builtins.input")
@patch("builtins.print")
def test_order_menu1(mock_print, mock_input):
    mock_input.return_value = 0
    order_menu()
    mock_print.assert_called_with("\nBack to Main Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu2(mock_print, mock_input):
    mock_input.return_value = 1
    order_menu()
    mock_print.assert_called_with("\nBack to Product Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu3(mock_print, mock_input):
    mock_input.return_value = 2
    order_menu()
    mock_print.assert_called_with("\nBack to Courier Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu4(mock_print, mock_input):
    mock_input.return_value = 3
    order_menu()
    mock_print.assert_called_with("\nCustomer Details\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu5(mock_print, mock_input):
    mock_input.return_value = 4
    order_menu()
    mock_print.assert_called_with("\nOrder Status Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu6(mock_print, mock_input):
    mock_input.return_value = 5
    order_menu()
    mock_print.assert_called_with("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_order_menu7(mock_print, mock_input):
    mock_input.return_value = str()
    order_menu()
    mock_print.assert_called_with("\nSelection not available. Please select a vaild number.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7