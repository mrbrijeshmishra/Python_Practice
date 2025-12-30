calc_logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(calc_logo, "\n\n")

def add(value1,value2):
    return value1+value2

def multiply(value1,value2):
    return value1 * value2

def div(value1,value2):
    return value1 / value2

def subtract(value1,value2):
    return value1 - value2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": div
}

def calculate():
    calculate_more = True

    value1 = float(input("What's the first number?: "))

    while calculate_more:
        for sign in operations:
            print(sign)

        operation_symbol = input("Pick an option: ")

        if operation_symbol in operations:

            value2 = float(input("What's the second number?: "))

            answer = (operations[operation_symbol](value1, value2))
            print(f"{value1} {operation_symbol} {value2} = {answer}")
            want_to_proceed = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")


            if want_to_proceed == 'y':
                value1 = answer
            else:
                calculate_more = False
                calculate()
        else:
            print("Wrong input!!! Try again")
            calculate()

calculate()
