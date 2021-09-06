from art_calc import logo


def add(a, b):
    return a+b


def subtract(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def multiply(a, b):
    return a * b


def division(a, b):
    if a > b:
        return a/b
    else:
        return b/a


calc_dict = {'+': add, '-': subtract, '*': multiply, '/': division}


def calculator():
    print(logo)
    end_of_calculation = True
    num1 = float(input("Enter the first number: "))

    for symbol in calc_dict:
        print(symbol)

    while end_of_calculation:
        operation_symbol = input("Pick one of the symbols from the line above: ")
        num2 = float(input("Enter the next number: "))
        symbol = calc_dict[operation_symbol]
        answer = symbol(num1, num2)

        print("{} {} {} = {}".format(num1, operation_symbol, num2, answer))

        user_in = input("Type 'y' to continue calculating with {} or type 'n' to start a new calculation: ")
        if user_in == 'y':
            num1 = answer
            end_of_calculation = True
        else:
            calculator()


calculator()
