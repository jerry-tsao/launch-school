'''
Internationalization 2

Building on your solutions from the previous exercises, write a function
local_greet that takes a locale as input, and returns a greeting. The locale
lets us greet people from different countries appropriately, even when they
share a common language, for example:

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
'''


lang_hello = {'en': 'Hi',
            'fr': 'Salut',
            'pt': 'Olá',
            'de': 'Hallo',
            'sv': 'Hej',
            'af': 'Haai',
}

region_hello = {'US': 'Hey',
                'GB': 'Hello',
                'AU': 'Howdy',
}

def extract_language(locale):
    return locale[:2]

def extract_region(locale):
    return locale[3:5]

def greet(greeting):
    return f'{greeting}!'

def local_greet(locale):
    lang = extract_language(locale)
    region = extract_region(locale)
    if region in region_hello:
        return greet(region_hello[region])
    else:
        return greet(lang_hello[lang])


print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-16'))
print(local_greet('af_ZA.UTF-8'))
