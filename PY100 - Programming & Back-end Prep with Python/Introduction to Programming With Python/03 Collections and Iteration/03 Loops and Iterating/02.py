'''
Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter.
The updated code should use a for loop to display the future ages.
'''

years = [10, 20, 30, 40]

def age(current_age):
    print(f'You are {current_age} years old.')
    for year in years:
        print(f'In {year} years, you will be {current_age + year} years old.')

current_age = int(input('How old are you? '))
print()
age(current_age)
