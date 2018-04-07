def roll_dice():
	"""Roll your dice like a player!"""
	from random import choice
	possibilities = [1,2,3,4,5,6]
	return choice(possibilities)