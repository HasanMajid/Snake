from point import Point


# Class for snake trail
class Trail:
    def __init__(self, trail=[]):
        self._trail = trail

    def __getitem__(self, index):
        return self._trail[index]
    
    def __len__(self):
        return len(self._trail)

    def shift_up(self, length):
        current_x = self._trail[0].x
        current_y = self._trail[0].y
        self._trail.insert(0, Point(current_x, current_y - 1))
        if len(self) != length:
            self._trail.pop()

    def shift_down(self, length):
        current_x = self._trail[0].x
        current_y = self._trail[0].y
        self._trail.insert(0, Point(current_x, current_y + 1))
        if len(self) != length:
            self._trail.pop()
            
    def shift_left(self, length):
        current_x = self._trail[0].x
        current_y = self._trail[0].y
        self._trail.insert(0, Point(current_x - 1, current_y))
        if len(self) != length:
            self._trail.pop()

    def shift_right(self, length):
        current_x = self._trail[0].x
        current_y = self._trail[0].y
        self._trail.insert(0, Point(current_x + 1, current_y))
        if len(self) != length:
            self._trail.pop()

    def has_point(self, point1):
        for point2 in self._trail:
            if point1 == point2:
                return True
        return False
