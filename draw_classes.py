import math
from math import sqrt


class Vector:
    def __init__(self, *pos):
        self.x = pos[0]
        self.y = pos[1]

    def dist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def scal(self, other):
        return self.x * other.x + self.y * other.y

    def __repr__(self):
        return "Vector({x},{y})".format(x=self.x, y=self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def rotate(self, digree):
        pi_angle = (digree / 360) * math.pi
        x = self.x * math.cos(pi_angle) - self.y * math.sin(pi_angle)
        y = self.x * math.sin(pi_angle) + self.y * math.cos(pi_angle)
        return Vector(x, y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def angle(self):
        return math.atan2(self.y, self.x) / math.pi * 180

    def normalized(self):
        length = self.length()
        if length < 1e-10:
            return Vector(0, 0)
        else:
            return self / length
