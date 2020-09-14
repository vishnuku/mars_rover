class Plateau(object):
    def __init__(self, plateau_size):
        self.plateau_size = plateau_size

    def set_robotic_rover(self, robotic_rover):
        self.robotic_rover = robotic_rover

    def move_robotic_rover(self, moves):
        for move in moves:
            if move == 'L' or move == 'R':
                self.robotic_rover.rotate(move)
            else: # M
                self.robotic_rover.move()