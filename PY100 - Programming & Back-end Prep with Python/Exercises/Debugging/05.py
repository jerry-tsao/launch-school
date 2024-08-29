'''
Confucius Says

You want to have a small script delivering motivational quotes, but with the
following code you run into a very common error message: TypeError: can only
concatenate str (not "NoneType") to str. What is the problem and how can you fix
it?

def get_quote(person):
    if person == 'Yoda':
        'Do. Or do not. There is no try.'
    if person == 'Confucius':
        'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
'''


'''
The problem is that in get_quote has no return value. To fix it, we must return
the quote, not just have the quote there.
'''


def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return ('I hear and I forget. I see and I remember. I do and I ' +
                'understand.')
    if person == 'Einstein':
        return ('Do not worry about your difficulties in Mathematics. I can ' +
                'assure you mine are still greater.')

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
