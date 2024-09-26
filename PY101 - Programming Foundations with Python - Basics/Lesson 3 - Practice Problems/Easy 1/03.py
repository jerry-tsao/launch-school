famous_words = "seven years ago..."

famous_words_v1 = f'Four score and {famous_words}'
famous_words_v2 = 'Four score and ' + famous_words
famous_words_v3 = 'Four score and {}'.format(famous_words)
famous_words_v4 = 'Four score and %s' % famous_words

print(famous_words_v1)
print(famous_words_v2)
print(famous_words_v3)
print(famous_words_v4)
