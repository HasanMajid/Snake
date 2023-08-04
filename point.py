import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        if point.x == self.x and point.y == self.y:
            return True
        return False
    
    @staticmethod
    def rand_point(min, max):
        return Point(random.randint(min, max), random.randint(min, max))
