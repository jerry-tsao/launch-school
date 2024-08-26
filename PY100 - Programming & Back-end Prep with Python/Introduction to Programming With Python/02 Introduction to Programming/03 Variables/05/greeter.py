'''
5. Write a program named greeter.py that greets 'Victor' three times. Your
program should use a variable and not hard code the string value 'Victor' in
each greeting. Here's an example run of the program:

$ python greeter.py
Good Morning, Victor.
Good Afternoon, Victor.
Good Evening, Victor.
'''

times_of_day = ['Morning', 'Afternoon', 'Evening']

def greet(name):
    for time_of_day in times_of_day:
        print(f'Good {time_of_day}, {name}.')

greet('Victor')
