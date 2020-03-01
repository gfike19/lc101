import random

class Point:

    def __init__(self, initX, initY):
            self.x = random.randrange(0,initX+1)
            self.y = random.randrange(0,initY+1)

p=Point(5)
q=Point(10)

print(p)
print(q)
