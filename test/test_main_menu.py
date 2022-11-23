from unittest.mock import patch

def main_menu():
    try:
            print("\nMain Menu Options\n")
            print("0 - Exit Application")
            print("1 - View Product Menu")
            print("2 - View Previous Orders\n")
            first_option = int(input("Enter a number: "))
            if first_option == 0:
                print("\nApplication Exited\n")
            elif first_option == 1:
                print("\nProduct Menu Options\n")
            elif first_option == 2:
                print("Previous Orders\n")
            else:
                print("\nSelection not available. Please select 0, 1 or 2.")
    except Exception as e:
        print("\nSelection not available. Please select a vaild number.")

@patch("builtins.input")
@patch("builtins.print")
def test_main_menu1(mock_print, mock_input):
    mock_input.return_value = 0
    main_menu()
    mock_print.assert_called_with("\nApplication Exited\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 5

@patch("builtins.input")
@patch("builtins.print")
def test_main_menu2(mock_print, mock_input):
    mock_input.return_value = 1
    main_menu()
    mock_print.assert_called_with("\nProduct Menu Options\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 5

@patch("builtins.input")
@patch("builtins.print")
def test_main_menu3(mock_print, mock_input):
    mock_input.return_value = 2
    main_menu()
    mock_print.assert_called_with("Previous Orders\n")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 5

@patch("builtins.input")
@patch("builtins.print")
def test_main_menu4(mock_print, mock_input):
    mock_input.return_value = str()
    main_menu()
    mock_print.assert_called_with("\nSelection not available. Please select a vaild number.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 5

@patch("builtins.input")
@patch("builtins.print")
def test_main_menu5(mock_print, mock_input):
    mock_input.return_value = 4
    main_menu()
    mock_print.assert_called_with("\nSelection not available. Please select 0, 1 or 2.")
    assert mock_input.call_count == 1
    assert mock_print.call_count == 5