'''
First Element

Write a function that returns the first element of a list provided as an
argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth

Be sure to handle the case where the input list is empty.
'''


def first(list):
    if list:
        return list[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))
print(first([]))
