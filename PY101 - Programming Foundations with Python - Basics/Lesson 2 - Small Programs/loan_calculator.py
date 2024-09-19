# Loan Calculator

import math
import os
from subprocess import call

info = {
    'loan_amount': '',
    'apr': '',
    'loan_duration_years': '',
    'loan_duration_months': '',
    'monthly_payment': '',
}

def reset_info():
    info['loan_amount'] = ''
    info['apr'] = ''
    info['loan_duration_years'] = ''
    info['loan_duration_months'] = ''
    info['monthly_payment'] = ''

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def display_info_block():
    loan_amount = info['loan_amount']
    apr = info['apr']
    loan_duration_years = info['loan_duration_years']
    loan_duration_months = info['loan_duration_months']
    monthly_payment = info['monthly_payment']

    print()
    print('-------------------------------------')
    print()
    print('   Welcome to the Loan Calculator!')
    print()
    print('-------------------------------------')
    print()
    print(f'   Loan amount: {loan_amount}')
    print(f'   APR: {apr}')
    print(f'   Loan duration (years): {loan_duration_years}')
    print(f'   Loan duration (months): {loan_duration_months}')
    print()
    print('-------------------------------------')
    print()
    print(f'   Monthly payment: {monthly_payment}')
    print()
    print('-------------------------------------')
    print()

def update_info_block():
    clear()
    display_info_block()

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
        print('What is the loan amount in dollars ($)?')
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
        print('What is the APR in percent (%)?')
        apr = input('APR: ')
        print()

        while invalid_apr(apr):
            print(f'{apr} is an invalid APR.')
            print()
            print('Please enter a valid APR of 0% or greater.')
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
        duration_type = input('(y/m): ').lower()
        print()
        while True:
            if duration_type.startswith('y') or duration_type.startswith('m'):
                break

            print('Please enter "y" or "m".')
            duration_type = input('(y/m): ').lower()
            print()

        duration_type = duration_type[0]

        print('What is the loan duration in '
              f'{'years' if duration_type == 'y' else 'months'}?')
        loan_duration = input('#: ')
        print()

        while invalid_number(loan_duration):
            print(f'{loan_duration} is an invalid loan duration.')
            print()
            print('Please enter a valid loan duration greater than 0.')
            loan_duration = input('#: ')
            print()

        loan_duration_cleaned = loan_duration.replace('$', '').replace(',', '')

        loan_duration_years = (
            float(loan_duration_cleaned) if duration_type == 'y'
            else float(loan_duration_cleaned) / 12)

        loan_duration_months = (
            float(loan_duration_cleaned) if duration_type == 'm'
            else float(loan_duration_cleaned) * 12)

        print(f'Your loan duration is {loan_duration_years:,.2f} year(s) or '
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
    clear()
    display_info_block()

    loan_amount = get_loan_amount()
    info['loan_amount'] = f'${loan_amount:,.2f}'
    update_info_block()

    apr = get_apr()
    info['apr'] = f'{apr:,.3f}%'
    update_info_block()

    loan_duration_years, loan_duration_months = get_loan_duration()
    info['loan_duration_years'] = f'{loan_duration_years:,.2f}'
    info['loan_duration_months'] = f'{loan_duration_months:,.0f}'
    update_info_block()

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                loan_duration_months)
    info['monthly_payment'] = f'${monthly_payment:,.2f}'
    update_info_block()

    print('Thank you for using the loan calculator!')
    print()

def new_calculation():
    while True:
        print('Would you like to calculate another monthly payment? (y/n)')

        answer = check_y_n()

        if answer == 'n':
            clear()
            break

        reset_info()
        loan_calculator()

def main():
    loan_calculator()
    new_calculation()

if __name__ == '__main__':
    main()
