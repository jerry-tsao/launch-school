'''
9. Repeat the previous question but, this time, use augmented assignment to
compute the final result, one year at a time.
'''

starting_balance = 1000.00
interest_rate = 0.05

print(f'Starting balance: {starting_balance}')

balance = starting_balance
balance *= (1 + interest_rate)
print(f'Balance after 1 year: {balance}')

balance *= (1 + interest_rate)
print(f'Balance after 2 years: {balance}')

balance *= (1 + interest_rate)
print(f'Balance after 3 years: {balance}')

balance *= (1 + interest_rate)
print(f'Balance after 4 years: {balance}')

balance *= (1 + interest_rate)
print(f'Balance after 5 years: {balance}')
