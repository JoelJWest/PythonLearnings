import math

class Sphere:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 4.0/3.0 * math.pi * (pow(self.r, 3))
