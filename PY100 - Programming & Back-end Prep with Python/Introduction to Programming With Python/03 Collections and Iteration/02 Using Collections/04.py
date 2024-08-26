'''
4. This is a 3-part question. Consider the following dictionary:

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

Part 1: Write some code to print Bark by accessing the element associated with
the key Dog.

Part 2: Write some code to print None when you try to print the value associated
with the non-existent key, Lizard.

Part 3: Write some code to print <silence> when you try to print the value
associated with the non-existent key, Lizard.
'''

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])

print(pets.get('Lizard'))

print(pets.get('Lizard', '<silence>'))
