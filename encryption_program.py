#encryption_program

import string
import random

#defining all characters
chars = " " + string.punctuation + string.ascii_letters + string.digits

#assigning all characters into a list
chars = list(chars)

#copying the list into key variable
key = chars.copy()

#shuffling the key
random.shuffle(key)

plain_text = input('Enter a message: ')
cipher_text = ""

#iterating over each letter via for loop
for letter in plain_text:
	index = chars.index(letter)
	cipher_text += key[index]

print(f'original message: {plain_text}')
print(f'encrypted message: {cipher_text}')