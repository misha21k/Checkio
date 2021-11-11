def sun_angle(time):
	hours, minutes = time.split(':')
	angle = 15*(int(hours) - 6) + 0.25*int(minutes)
	return angle if 0 <= angle <= 180 else 'I don\'t see the sun!'


if __name__ == '__main__':
	print("Example:")
	print(sun_angle("07:00"))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert sun_angle("07:00") == 15
	assert sun_angle("01:23") == "I don't see the sun!"
	print("Coding complete? Click 'Check' to earn cool rewards!")