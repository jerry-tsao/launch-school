'''
Dictionary Access

You are trying to access a value in a dictionary, but the code is giving you an
error. Can you change line 3 so that it prints "Unknown" instead of raising an
error?

1| info = {'name': 'Srdjan', 'age': 38}
2| 
3| print(info['city'])
'''


info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))
