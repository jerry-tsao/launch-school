'''
Squared Number

Write a function that accepts a single argument, a number, and returns the
result of multiplying its argument by an exponent of 2 (also known as squaring
the number or raising the number to the power of 2).

squared_number(3)   # 9
'''

def squared_num(num):
    square = num**2
    return square

print(squared_num(3))
