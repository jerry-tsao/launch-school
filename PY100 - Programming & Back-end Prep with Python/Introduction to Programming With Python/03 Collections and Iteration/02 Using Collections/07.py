'''
7. Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
'''

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

substrings = info.split(':')
new_string = '+'.join(substrings)
print(new_string)

new_string2 = info.replace(':', '+')
print(new_string2)
