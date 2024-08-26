'''
2. This question may be a little challenging if your math skills are rusty.
Don't be afraid to take advantage of the hints. Try your best to solve the
problem, but don't feel compelled to complete it if you become frustrated.

Use the REPL and the arithmetic operators to extract the individual digits of
4936:

    1. One place is 6.
    2. Tens place is 3.
    3. Hundreds place is 9.
    4. Thousands place is 4.

Each digit may require multiple Python statements.
'''

num = 4936

ones = num % 10
tens = (num // 10) % 10
hundreds = (num // 100) % 10
thousands = (num // 1000)

print(f'Ones place is {ones}')
print(f'Tens places is {tens}')
print(f'Hundreds place is {hundreds}')
print(f'Thousands place is {thousands}')
