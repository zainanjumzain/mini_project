from unittest.mock import patch

def courier_menu():
    try:
        print("\nCourier Menu Options\n")
        print("0 - Go back to Main Menu")
        print("1 - Go back to Product Menu")
        print("2 - Add or Change Courier")
        print("3 - View current Courier")
        print("4 - Go to Order Menu\n")
        courier_option = int(input("Enter a number: "))
        if courier_option == 0:
            print("\nBack to Main Menu\n")
        elif courier_option == 1:
            print("\nBack to Product Menu\n")
        elif courier_option == 2:
            print("\nCourier Options\n")
        elif courier_option == 3:
            print("courier")   
        elif courier_option == 4:
            print("\nOrder Menu\n")
        else:
            print("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
    except Exception as e:
        print("\nSelection not available. Please select a vaild number.") and courier_menu()

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu1(mock_print, mock_input):
    mock_input.return_value = 0
    courier_menu()
    mock_print.assert_called_with("\nBack to Main Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu2(mock_print, mock_input):
    mock_input.return_value = 1
    courier_menu()
    mock_print.assert_called_with("\nBack to Product Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu3(mock_print, mock_input):
    mock_input.return_value = 2
    courier_menu()
    mock_print.assert_called_with("\nCourier Options\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu4(mock_print, mock_input):
    mock_input.return_value = 3
    courier_menu()
    mock_print.assert_called_with("courier")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu5(mock_print, mock_input):
    mock_input.return_value = 4
    courier_menu()
    mock_print.assert_called_with("\nOrder Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu6(mock_print, mock_input):
    mock_input.return_value = 5
    courier_menu()
    mock_print.assert_called_with("\nSelection not available. Please select 0, 1, 2, 3 or 4.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7

@patch("builtins.input")
@patch("builtins.print")
def test_courier_menu7(mock_print, mock_input):
    mock_input.return_value = str()
    courier_menu()
    mock_print.assert_called_with("\nSelection not available. Please select a vaild number.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 7