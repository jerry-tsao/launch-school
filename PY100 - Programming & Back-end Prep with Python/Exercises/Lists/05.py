'''
Filter

Count the number of elements in scores that are 100 or above.
'''

scores = [96, 47, 113, 89, 100, 102]


print(sum(1 for score in scores if score >= 100))
