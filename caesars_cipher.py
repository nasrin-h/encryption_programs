#caesar's cipher

import string 

#input message
plain_text = input('please enter a message: ')

#encryption/decryption key
key = 4

# switch mode between encrypt/decrypt
mode = 'encrypt'

#defining all possible characters
chars = string.ascii_letters + string.digits

#output message
cipher_text = ''

#iterating over each character using for loop
for char in plain_text:
	inputIndex = chars.find(char)
	#encryption/decryption 
	if mode == 'encrypt':
		outputIndex = inputIndex + key
	elif mode == 'decrypt':
		outputIndex = inputIndex - key
	#wraparound
	if outputIndex >= len(chars):
		outputIndex= outputIndex - len(chars)
	elif outputIndex < 0:
		outputIndex = outputIndex + len(chars)
	cipher_text = cipher_text + chars[outputIndex]

print(cipher_text)