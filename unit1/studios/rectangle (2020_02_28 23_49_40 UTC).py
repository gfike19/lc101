class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def getPerimeter(self):
        return (2 * self.length) + (2 * self.width)
    
    def getArea(self):
        return self.length * self.width
    
    def isSquare(self):
        if self.length == self.width:
            return True
        else:
            False