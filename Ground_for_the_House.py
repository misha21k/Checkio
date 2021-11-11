def house(plan):
	i = j = 0
	home = []
	for char in plan:
		if char == '#':
			home.append((i, j))
		elif char == '\n':
			i += 1
			j = 0
		j += 1
	i_lam = lambda item: item[0]
	j_lam = lambda item: item[1]
	try:
		width = max(home, key=i_lam)[0] - min(home, key=i_lam)[0] + 1
		height = max(home, key=j_lam)[1] - min(home, key=j_lam)[1] + 1
		return width*height
	except ValueError:
		return 0


if __name__ == '__main__':
	print("Example:")
	print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

	assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

	assert house('''0000
0000
#000
''') == 1

	assert house('''0000
0000
''') == 0

	assert house('''
0##0
0000
#00#
''') == 12

	print("Coding complete? Click 'Check' to earn cool rewards!")