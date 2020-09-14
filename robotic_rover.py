class RoboticRover(object):
    #Initialize dic for left rotatation combination
    rotate_left = {
        'N' : 'W',
        'E' : 'N',
        'W' : 'S',
        'S' : 'E'
    }

    #Initialize dic for right rotatation combination
    rotate_right = {
        'N' : 'E',
        'E' : 'S',
        'W' : 'N',
        'S' : 'W'
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y = self.y + 1
        elif self.direction == 'E':
            self.x = self.x + 1
        elif self.direction == 'W':
            self.x = self.x - 1
        elif self.direction == 'S':
            self.y = self.y - 1

    def rotate(self,orientation):
        if orientation == 'L':
            self.direction = self.rotate_left[self.direction]
        else: # R
            self.direction = self.rotate_right[self.direction]

    def __str__(self):
        return '%d %d %c' % (self.x, self.y, self.direction)