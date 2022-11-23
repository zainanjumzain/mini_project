from unittest.mock import patch

def order_status():
    try:
        print("\nOrder Status Menu Options\n")
        print("0 - Go back to Main Menu")
        print("1 - Go back to Product Menu")
        print("2 - Go back to Courier Menu")
        print("3 - Go back To Order Menu")
        print("4 - Update Order Status")
        print("5 - View Final Order")
        print("6 - Mark Current Order as Completed\n")
        fourth_option = int(input("Enter a number: "))
        if fourth_option == 0:
            print("\nBack to Main Menu\n")
        elif fourth_option == 1:
            print("\nBack to Product Menu\n")
        elif fourth_option == 2:
            print("\nBack to Courier Menu\n")            
        elif fourth_option == 3:
            print("\nBack To Order Menu\n")
        elif fourth_option == 4:
            print("\nUpdate Order Status\n")       
        elif fourth_option == 5:
            print("\n Final Order: ")
        elif fourth_option == 6:
            print("\nOrder Marked as Complete\n")
        else:
            print("\nSelection not available. Please select 0, 1, 2, 3, 4, 5 or 6.")
    except Exception as e:
        print("\nSelection not available. Please select a vaild number.") and order_status()
                 
@patch("builtins.input")
@patch("builtins.print")
def test_order_status1(mock_print, mock_input):
    mock_input.return_value = 0
    order_status()
    mock_print.assert_called_with("\nBack to Main Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status2(mock_print, mock_input):
    mock_input.return_value = 1
    order_status()
    mock_print.assert_called_with("\nBack to Product Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status3(mock_print, mock_input):
    mock_input.return_value = 2
    order_status()
    mock_print.assert_called_with("\nBack to Courier Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status4(mock_print, mock_input):
    mock_input.return_value = 3
    order_status()
    mock_print.assert_called_with("\nBack To Order Menu\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status5(mock_print, mock_input):
    mock_input.return_value = 4
    order_status()
    mock_print.assert_called_with("\nUpdate Order Status\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status6(mock_print, mock_input):
    mock_input.return_value = 5
    order_status()
    mock_print.assert_called_with("\n Final Order: ")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status7(mock_print, mock_input):
    mock_input.return_value = 6
    order_status()
    mock_print.assert_called_with("\nOrder Marked as Complete\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status8(mock_print, mock_input):
    mock_input.return_value = 7
    order_status()
    mock_print.assert_called_with("\nSelection not available. Please select 0, 1, 2, 3, 4, 5 or 6.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9

@patch("builtins.input")
@patch("builtins.print")
def test_order_status9(mock_print, mock_input):
    mock_input.return_value = str()
    order_status()
    mock_print.assert_called_with("\nSelection not available. Please select a vaild number.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 9