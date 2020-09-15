
class Dot:
    def __init__(self, x, y, r, g, b, i, j):
        self.r = r
        self.g = g
        self.b = b
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.infected = 0
        self.sick = -1

    def setRGB(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Line:
    def __init__(self, x1, y1, x2, y2, r, g, b, t):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.r = r
        self.g = g
        self.b = b
        self.t = t

