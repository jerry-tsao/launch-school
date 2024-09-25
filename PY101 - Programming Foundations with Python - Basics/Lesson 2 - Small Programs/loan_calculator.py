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

def update_info_block(k, v):
    info[k] = v
    clear()
    display_info_block()

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
        prompt('Is this correct? (y/n)')

        answer = check_y_n()

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
        prompt('Is this correct? (y/n)')

        answer = check_y_n()

        if answer == 'y':
            break

    return float(apr)

def get_loan_duration():
    while True:
        prompt('Would you like to enter the loan duration in years or months?')
        prompt('Enter "y" for years or "m" for months.')
        duration_type = input('(y/m): ')
        duration_type_lower = duration_type.lower()
        blank_line()
        while True:
            if (duration_type_lower.startswith('y') or
                duration_type_lower.startswith('m')):
                break

            prompt(f'{duration_type} is an invalid response.')
            blank_line()
            prompt('Please enter "y" or "m".')
            duration_type = input('(y/m): ')
            duration_type_lower = duration_type.lower()
            blank_line()

        duration_type_code = duration_type_lower[0]

        prompt('What is the loan duration in '
              f'{'years' if duration_type_code == 'y' else 'months'}?')
        loan_duration = input('#: ')
        blank_line()

        while invalid_number(loan_duration):
            prompt(f'{loan_duration} is an invalid loan '
                   'duration.')
            blank_line()
            prompt('Please enter a valid loan duration greater than 0.')
            loan_duration = input('#: ')
            blank_line()

        loan_duration_cleaned = loan_duration.replace('$', '').replace(',', '')

        loan_duration_years = (
            float(loan_duration_cleaned) if duration_type_code == 'y'
            else float(loan_duration_cleaned) / 12)

        loan_duration_months = (
            float(loan_duration_cleaned) if duration_type_code == 'm'
            else float(loan_duration_cleaned) * 12)

        prompt(f'Your loan duration is {loan_duration_years:,.2f} year(s) or '
            f'{loan_duration_months:,.0f} month(s).')
        prompt('Is this correct? (y/n)')

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
    update_info_block('loan_amount', f'${loan_amount:,.2f}')

    apr = get_apr()
    update_info_block('apr', f'{apr:,.3f}%')

    loan_duration_years, loan_duration_months = get_loan_duration()
    update_info_block('loan_duration_years', f'{loan_duration_years:,.2f}')
    update_info_block('loan_duration_months', f'{loan_duration_months:,.0f}')

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                loan_duration_months)
    update_info_block('monthly_payment', f'${monthly_payment:,.2f}')

    prompt('Thank you for using the loan calculator!')
    blank_line()

def new_calculation():
    while True:
        prompt('Would you like to calculate another monthly payment? (y/n)')

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
