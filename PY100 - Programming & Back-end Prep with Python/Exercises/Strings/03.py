'''
Ignoring Case

Using the following code, compare the value of name with the string 'RoGeR'
while ignoring the case of both strings. Print true if the values are the same;
print false if they aren't. Next, perform a case-insensitive comparison between
the value of name and the string 'DAVE'.
'''


name = 'Roger'

print(name.casefold() == 'RoGeR'.casefold())
print(name.casefold() == 'DAVE'.casefold())
