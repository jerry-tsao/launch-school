# Info needed:
# - loan amount
# - Annual Percentage Rate (APR)
# - loan duration

# Calculate the following:
# - monthly interest rate (APR / 12)
# - loan duration in months

# Formula:
# m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months


def invalid_number(num):
    try:
        number = float(num)
        if number < 0:
            raise ValueError('The number cannot be negative.')
    except ValueError:
        return True

    return False

def get_loan_amount():
    loan_amount = input('Loan amount: $')

    while invalid_number(loan_amount):
        print('Please enter a valid loan amount.')
        loan_amount = input('Loan amount: $')

    return float(loan_amount)

def get_apr():
    apr = input('APR in % ("3.25" for 3.25%): ')

    while invalid_number(apr):
        print('Please enter a valid APR.')
        apr = input('APR in %: ')

    return float(apr)

def get_loan_duration():
    loan_duration = input('Loan duration in years: ')

    while invalid_number(loan_duration):
        print('Please enter a valid loan duration.')
        loan_duration = input('Loan duration in years: ')

    return float(loan_duration)

def calculate_monthly_payment(loan_amount, apr, loan_duration):
    apr_percent = apr / 100
    monthly_interest_rate = apr_percent / 12
    loan_duration_months = loan_duration * 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / loan_duration_months
    else:
        monthly_payment = loan_amount * (monthly_interest_rate /
                                        (1 -
                                        (1 + monthly_interest_rate)**
                                        (-loan_duration_months)))

    return monthly_payment

def loan_calculator():
    loan_amount = get_loan_amount()
    apr = get_apr()
    loan_duration = get_loan_duration()
    loan_duration_months = loan_duration * 12

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                apr,
                                                loan_duration)

    print(f'The monthly payment for your loan of ${loan_amount:,.2f} at '
          f'{apr:,.3f}% APR over {loan_duration:,.1f} years '
          f'({loan_duration_months:,.0f} months) is ${monthly_payment:,.2f}.')

loan_calculator()
