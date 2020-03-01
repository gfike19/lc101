import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

    def reflect_x(self):
        self.y = -1*(self.y)
        return self.x,self.y

    def slopeFromOrigin(self):
        return (self.y-0)/(self.x-0)

    def get_line_to(self,otherP):
        m = (self.y-otherP.getY())/(self.x-otherP.getX())
        b = -1((m*self.x)-self.y)
        return b

p = Point(3, 3)
q = Point(6, 7)
print(p.get_line_to(q))
