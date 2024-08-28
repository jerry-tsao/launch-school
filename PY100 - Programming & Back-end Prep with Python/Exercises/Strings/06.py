'''
Is Empty?

Write a function that checks whether a string is empty or not. For example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
'''


def is_empty(string):
    return len(string) == 0

print(is_empty('mars'))
print(is_empty('  '))
print(is_empty(''))
