def to_encrypt(text, delta):
	cipher = ''
	for char in text:
		if char != ' ':
			delta1 = delta
			if ord(char) + delta1 > ord('z'):
				delta1 -= ord('z') - ord('a') + 1
			elif ord(char) + delta1 < ord('a'):
				delta1 += ord('z') - ord('a') + 1
			cipher += chr(ord(char) + delta1)
		else:
			cipher += char
	return cipher


if __name__ == '__main__':
	print("Example:")
	print(to_encrypt('abc', 10))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert to_encrypt("a b c", 3) == "d e f"
	assert to_encrypt("a b c", -3) == "x y z"
	assert to_encrypt("simple text", 16) == "iycfbu junj"
	assert to_encrypt("important text", 10) == "swzybdkxd dohd"
	assert to_encrypt("state secret", -13) == "fgngr frperg"
	print("Coding complete? Click 'Check' to earn cool rewards!")