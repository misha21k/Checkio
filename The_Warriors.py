class Warrior:
	live = 50
	attack = 5

	@property
	def is_alive(self):
		return self.live > 0


class Knight(Warrior):
	attack = 7


def fight(unit_1, unit_2):
	first_beats = True
	while True:
		if first_beats:
			unit_2.live -= unit_1.attack
			if unit_2.live <= 0:
				return True
			first_beats = False
		else:
			unit_1.live -= unit_2.attack
			if unit_1.live <= 0:
				return False
			first_beats = True


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	print("Coding complete? Let's try tests!")