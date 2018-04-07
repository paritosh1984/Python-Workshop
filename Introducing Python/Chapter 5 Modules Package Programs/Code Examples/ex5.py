from roll import *

side = single.roll_dice()
print("You have rolled a {}".format(side))

sides = double.roll_dice()
print("You have rolled {} and {}".format(sides[0],sides[1]))