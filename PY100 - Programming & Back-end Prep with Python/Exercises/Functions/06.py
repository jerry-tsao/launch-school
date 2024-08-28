'''
Three-way Comparison

Write a function that compares the length of two strings. It should return -1 if
the first string is shorter, 1 if the second string is shorter, and 0 if they're
of equal length. For example:

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0
'''

def compare_by_length(string1, string2):
    length_diff = len(string1) - len(string2)
    result = length_diff and length_diff // abs(length_diff)
    return result

print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))
