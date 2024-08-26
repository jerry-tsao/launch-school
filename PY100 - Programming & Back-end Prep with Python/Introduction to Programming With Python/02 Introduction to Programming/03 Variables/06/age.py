'''
6. Write a program named age.py that includes someone's age and then calculates
and reports the future age 10, 20, 30, and 40 years from now. Here's the output
for someone who is 22 years old.

You are 22 years old.
In 10 years, you will be 32 years old.
In 20 years, you will be 42 years old.
In 30 years, you will be 52 years old.
In 40 years, you will be 62 years old.
'''

years = [10, 20, 30, 40]

def age(current_age):
    print(f'You are {current_age} years old.')
    for year in years:
        print(f'In {year} years, you will be {current_age + year} years old.')

age(22)
