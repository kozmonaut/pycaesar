
# Show menu options
def main():
	while True:
		print ('Choose 1) Encrypt or 2) Decrypt')
		option = raw_input()

		if option in '1 2'.split():
			return option
		else:
			print 'Choose something'

# Type key vaule for shifting
def getKey():
	print ('Enter the key number (1-26)')
	key = int(raw_input())
	return key

# Type message to encrypt/decrypt
def getMessage():
	print ('Enter your message')
	message= raw_input()
	return message

# Caesar start
def caesar(o, m, k):
	# If you want to decrypt
	if o == '2':
		k = -k

	# Empty text container
	ciphertext = ''
		
	for symbol in m:

		if symbol.isalpha():
			num = ord(symbol) + k

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26

			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			ciphertext  += chr(num)
		else:
			ciphertext += symbol

	return ciphertext 

o = main()
m = getMessage()
k = getKey()

if __name__ == '__main__':
    print 'New message is:'
    print (caesar(o,m,k))