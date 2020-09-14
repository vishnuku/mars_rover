from plateau import Plateau
from robotic_rover import RoboticRover

#Initialize
inilitize = '5 5'

plateau_size = map(int, inilitize.split())
plateau = Plateau(plateau_size)


def test_rover(line1, line2):
	(x, y, d) = line1.split()
	moves = line2.strip()

	robotic_rover = RoboticRover(int(x), int(y), d)
	plateau.set_robotic_rover(robotic_rover)
	plateau.move_robotic_rover(moves)
	return robotic_rover

#first line test
line1 = '1 2 N'
line2 = 'LMLMLMLMM'

print("Position after first input {}".format(test_rover(line1, line2)))

 
#second line test
line1 = '3 3 E'
line2 = 'MMRMMRMRRM'

print("Position after second input:   {}".format(test_rover(line1, line2)))
