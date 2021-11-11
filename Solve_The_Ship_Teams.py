def two_teams(sailors):
	first_ship = []
	second_ship = []
	for key, item in sailors.items():
		if sailors[key] < 20 or sailors[key] > 40:
			first_ship.append(key)
		else:
			second_ship.append(key)
	first_ship.sort()
	second_ship.sort()

	return [
		first_ship,
		second_ship
	]

if __name__ == '__main__':
	print("Example:")
	print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert two_teams({
		'Smith': 34,
		'Wesson': 22,
		'Coleman': 45,
		'Abrahams': 19}) == [
			['Abrahams', 'Coleman'],
			['Smith', 'Wesson']
			]

	assert two_teams({
		'Fernandes': 18,
		'Johnson': 22,
		'Kale': 41,
		'McCortney': 54}) == [
			['Fernandes', 'Kale', 'McCortney'],
			['Johnson']
			]
	print("Coding complete? Click 'Check' to earn cool rewards!")