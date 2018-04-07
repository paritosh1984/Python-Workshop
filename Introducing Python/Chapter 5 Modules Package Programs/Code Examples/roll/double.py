def roll_dice():
	"""Why stop with one, when you can roll a pair of dice!"""
	from random import choice
	possibilites = [1,2,3,4,5,6]
	return(choice([(one, two) for one in possibilites for two in possibilites]))