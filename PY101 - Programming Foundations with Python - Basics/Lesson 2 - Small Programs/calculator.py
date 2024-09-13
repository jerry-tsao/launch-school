import json

LANGUAGE = 'en'

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)[LANGUAGE]

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])

while True:

    # Ask the user for the first number.
    prompt(MESSAGES['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    # Ask the user for the second number.
    prompt(MESSAGES['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    # Ask the user for an operation to perform.
    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['operation_error'])
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':   # '1' represents addition
            output = float(number1) + float(number2)
        case '2':   # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3':   # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4':   # '4' represents division
            output = float(number1) / float(number2)

    # Print the result to the terminal.
    prompt(eval(MESSAGES['result']))

    prompt(MESSAGES['another_calculation'])
    response = input()

    if response != 'y':
        break
