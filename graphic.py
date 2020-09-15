
class Dot:
    def __init__(self, x, y, r, g, b, i, j):
        self.r = r
        self.g = g
        self.b = b
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.infected = False

    def setRGB(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getX(self):
        return self.x
    def getY(self):
        return self.y



