'''
Populate List

You want to add the numbers from 1 to 5 to a list, but the code below is not
producing the expected result. How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
'''

'''
The code will add the numbers 0 to 4. To add the numbers 1 to 5, we just need
to shift the range by one.
'''


numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)
