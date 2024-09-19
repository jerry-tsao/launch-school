# Loan Calculator

import math
import os
from subprocess import call

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def welcome():
    clear()
    print()
    print('-------------------------------------')
    print('   Welcome to the Loan Calculator!')
    print('-------------------------------------')
    print()

def invalid_number(num):
    try:
        number = float(num.replace('$', '').replace(',', ''))
        if number <= 0:
            raise ValueError('The number must be positive.')
        if number == float('inf'):
            raise ValueError('The number cannot be infinite.')
        if math.isnan(number):
            raise ValueError('The number cannot be NaN.')
    except ValueError:
        return True

    return False

def invalid_apr(num):
    try:
        number = float(num.replace('%', '').replace(',', ''))
        if number < 0:
            raise ValueError('The number cannot be negative.')
        if number == float('inf'):
            raise ValueError('The number cannot be infinite.')
        if math.isnan(number):
            raise ValueError('The number cannot be NaN.')
    except ValueError:
        return True

    return False

def check_y_n():
    answer = input('(y/n): ').lower()
    print()

    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break

        print('Please enter "y" or "n".')
        answer = input('(y/n): ').lower()
        print()

    return answer[0]

def get_loan_amount():
    while True:
        print('What is the loan amount?')
        loan_amount = input('Loan amount: $')
        print()

        while invalid_number(loan_amount):
            print(f'${loan_amount} is an invalid loan amount.')
            print()
            print('Please enter a loan amount greater than $0.')
            loan_amount = input('Loan amount: $')
            print()

        loan_amount_cleaned = loan_amount.replace('$', '').replace(',', '')

        print(f'Your loan amount is ${float(loan_amount_cleaned):,.2f}.')
        print('Is this correct? (y/n)')

        answer = check_y_n()

        if answer == 'y':
            break

    return float(loan_amount_cleaned)

def get_apr():
    while True:
        print('What is the APR in %?')
        apr = input('APR: ')
        print()

        while invalid_apr(apr):
            print(f'{apr} is an invalid APR.')
            print()
            print('Please enter a valid APR of 0% or greater (numbers only).')
            apr = input('APR: ')
            print()

        apr_cleaned = apr.replace('%', '').replace(',', '')

        print(f'Your APR is {float(apr_cleaned):,.3f}%.')
        print('Is this correct? (y/n)')

        answer = check_y_n()

        if answer == 'y':
            break

    return float(apr)

def get_loan_duration():
    while True:
        print('Would you like to enter the loan duration in years or months?')
        print('Enter "y" for years or "m" for months.')
        duration_type = input('Years or months: ').lower()
        print()
        while True:
            if duration_type.startswith('y') or duration_type.startswith('m'):
                break

            print('Please enter "y" or "m".')
            duration_type = input('Years or months: ').lower()
            print()

        duration_type = duration_type[0]

        print('What is the loan duration?')
        loan_duration = input('Loan duration: ')
        print()

        while invalid_number(loan_duration):
            print(f'{loan_duration} is an invalid loan duration.')
            print()
            print('Please enter a valid loan duration greater than 0.')
            loan_duration = input('Loan duration: ')
            print()

        loan_duration_cleaned = loan_duration.replace('$', '').replace(',', '')

        loan_duration_years = (
            float(loan_duration_cleaned) if duration_type == 'y'
            else float(loan_duration_cleaned) / 12)

        loan_duration_months = (
            float(loan_duration_cleaned) if duration_type == 'm'
            else float(loan_duration_cleaned) * 12)

        print(f'Your loan duration is {loan_duration_years:,.1f} year(s) or '
            f'{loan_duration_months:,.0f} month(s).')
        print('Is this correct? (y/n)')

        answer = check_y_n()

        if answer == 'y':
            break

    return (loan_duration_years, loan_duration_months)

def calculate_monthly_payment(loan_amount, apr, loan_duration_months):
    apr_percent = apr / 100
    monthly_interest_rate = apr_percent / 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / loan_duration_months
    else:
        monthly_payment = loan_amount * (monthly_interest_rate /
                                         (1 -
                                         (1 + monthly_interest_rate)**
                                         (-loan_duration_months)))

    return monthly_payment

def loan_calculator():
    welcome()

    loan_amount = get_loan_amount()
    welcome()
    print(f'   Loan amount: ${loan_amount:,.2f}')
    print()
    print('-------------------------------------')
    print()

    apr = get_apr()
    welcome()
    print(f'   Loan amount: ${loan_amount:,.2f}')
    print(f'   APR: {apr:,.3f}%')
    print()
    print('-------------------------------------')
    print()

    loan_duration_years, loan_duration_months = get_loan_duration()
    welcome()
    print(f'   Loan amount: ${loan_amount:,.2f}')
    print(f'   APR: {apr:,.3f}%')
    print(f'   Loan duration (years): {loan_duration_years:,.1f}')
    print(f'   Loan duration (months): {loan_duration_months:,.0f}')
    print()

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                loan_duration_months)

    print('-------------------------------------')
    print(f'   Monthly payment: ${monthly_payment:,.2f}')
    print('-------------------------------------')
    print()

while True:
    loan_calculator()

    print('Thank you for using the loan calculator!')
    print()
    print('Would you like to calculate another monthly payment? (y/n)')

    ans = check_y_n()

    if ans == 'n':
        break
