'''
Last Element

Write a function that returns the last element of a list provided as an
argument. For example:

print(last(['Earth', 'Moon', 'Mars']))  # Mars

Be sure to handle the case where the input list is empty.
'''


def last(list):
    if list:
        return list[-1]
    else:
        return None
    
print(last(['Earth', 'Moon', 'Mars']))
print(last([]))
