'''
Is Empty or Blank?

Write an is_empty_or_blank function to determine whether a string is either
empty or consists entirely of spaces. For example:

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
'''


def is_empty_or_blank(string):
    return len(string.strip(' ')) == 0

print(is_empty_or_blank('mars'))
print(is_empty_or_blank('  '))
print(is_empty_or_blank(''))
