# Loan Calculator

import math
import os
from subprocess import call

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def new_loan_info():
    loan_info = {
        'loan_amount': '',
        'apr': '',
        'loan_duration_years': '',
        'loan_duration_months': '',
        'monthly_payment': '',
    }

    return loan_info

def display_info_block(loan_info):
    loan_amount = loan_info['loan_amount']
    apr = loan_info['apr']
    loan_duration_years = loan_info['loan_duration_years']
    loan_duration_months = loan_info['loan_duration_months']
    monthly_payment = loan_info['monthly_payment']

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

def update_info_block(loan_info, k, v):
    loan_info[k] = v
    clear()
    display_info_block(loan_info)

def prompt(message):
    print(message)

def blank_line():
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
    while True:
        answer = input('(y/n): ')
        answer_lower = answer.lower()
        blank_line()

        if answer_lower.startswith('y') or answer_lower.startswith('n'):
            break

        prompt(f'{answer} is an invalid response.')
        prompt('Please enter "y" or "n".')

    return answer_lower[0]

def confirm_data_input():
    prompt('Is this correct? (y/n)')

    answer = check_y_n()

    return answer

def get_loan_amount():
    while True:
        prompt('What is the loan amount in dollars ($)?')
        loan_amount = input('Loan amount: $')
        blank_line()

        while invalid_number(loan_amount):
            prompt(f'${loan_amount} is an invalid loan amount.')
            blank_line()
            prompt('Please enter a loan amount greater than $0.')
            loan_amount = input('Loan amount: $')
            blank_line()

        loan_amount_cleaned = loan_amount.replace('$', '').replace(',', '')

        prompt(f'Your loan amount is ${float(loan_amount_cleaned):,.2f}.')

        answer = confirm_data_input()

        if answer == 'y':
            break

    return float(loan_amount_cleaned)

def get_apr():
    while True:
        prompt('What is the APR in percent (%)?')
        apr = input('APR: ')
        blank_line()

        while invalid_apr(apr):
            prompt(f'{apr} is an invalid APR.')
            blank_line()
            prompt('Please enter a valid APR of 0% or greater.')
            apr = input('APR: ')
            blank_line()

        apr_cleaned = apr.replace('%', '').replace(',', '')

        prompt(f'Your APR is {float(apr_cleaned):,.3f}%.')

        answer = confirm_data_input()

        if answer == 'y':
            break

    return float(apr)

def get_loan_duration_type():
    prompt('Would you like to enter the loan duration in years or months?')
    prompt('Enter "y" for years or "m" for months.')
    while True:
        duration_type = input('(y/m): ')
        duration_type_lower = duration_type.lower()
        blank_line()
        if duration_type_lower in ('y', 'yr', 'yrs', 'year', 'years', 'm',
                                   'mo', 'mos', 'mon', 'mons', 'month',
                                   'months'):
            break

        prompt(f'{duration_type} is an invalid response.')
        blank_line()
        prompt('Please enter "y" or "m".')

    duration_type_code = duration_type_lower[0]

    return duration_type_code

def get_loan_duration_num(loan_duration_type):
    prompt('What is the loan duration in '
            f'{'years' if loan_duration_type == 'y' else 'months'}?')
    loan_duration_num = input('#: ')
    blank_line()

    while invalid_number(loan_duration_num):
        prompt(f'{loan_duration_num} is an invalid loan '
                'duration.')
        blank_line()
        prompt('Please enter a valid loan duration greater than 0.')
        loan_duration_num = input('#: ')
        blank_line()

    loan_duration_cleaned = loan_duration_num.replace('$', '').replace(',', '')

    return loan_duration_cleaned

def get_loan_duration():
    while True:
        loan_duration_type = get_loan_duration_type()
        loan_duration_num = get_loan_duration_num(loan_duration_type)

        loan_duration_years = (
            float(loan_duration_num) if loan_duration_type == 'y'
            else float(loan_duration_num) / 12)

        loan_duration_months = (
            float(loan_duration_num) if loan_duration_type == 'm'
            else float(loan_duration_num) * 12)

        prompt(f'Your loan duration is {loan_duration_years:,.2f} year(s) or '
            f'{loan_duration_months:,.0f} month(s).')

        answer = confirm_data_input()

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

    loan_info = new_loan_info()

    display_info_block(loan_info)

    loan_amount = get_loan_amount()
    update_info_block(loan_info, 'loan_amount', f'${loan_amount:,.2f}')

    apr = get_apr()
    update_info_block(loan_info, 'apr', f'{apr:,.3f}%')

    loan_duration_years, loan_duration_months = get_loan_duration()
    update_info_block(loan_info, 'loan_duration_years',
                      f'{loan_duration_years:,.2f}')
    update_info_block(loan_info, 'loan_duration_months',
                      f'{loan_duration_months:,.0f}')

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                loan_duration_months)
    update_info_block(loan_info, 'monthly_payment', f'${monthly_payment:,.2f}')

    prompt('Thank you for using the loan calculator!')
    blank_line()

def ask_calculate_again():
    prompt('Would you like to calculate another monthly payment? (y/n)')
    answer = check_y_n()

    return answer

def calculate_again():
    while True:
        answer = ask_calculate_again()

        if answer == 'n':
            clear()
            break

        loan_calculator()

def main():
    loan_calculator()
    calculate_again()

if __name__ == '__main__':
    main()
