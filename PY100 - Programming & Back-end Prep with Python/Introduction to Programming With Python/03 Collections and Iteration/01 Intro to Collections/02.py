'''
2. Can you write some code to change the value 'bye' in the following tuple to
'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

Note: this problem is a bit tricky.
'''

stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

print(stuff)