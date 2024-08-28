'''
Internationalization 1

Use Python's control structures to create a function that takes an ISO 639-1
language code and returns a greeting in that language. You can take the examples
below or add whatever languages you like.

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
'''


hello = {'en': 'Hi',
         'fr': 'Salut',
         'pt': 'Olá',
         'de': 'Hallo',
         'sv': 'Hej',
         'af': 'Haai',
}

def greet(lang):
    return f'{hello[lang]}!'

print(greet('en'))
print(greet('fr'))
print(greet('pt'))
print(greet('de'))
print(greet('sv'))
print(greet('af'))
