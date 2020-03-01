class Baseball:

    def __init__(self, name, num, hit):
        self.name = name
        self.num = num
        self.hit = hit
    
    def setHits(self, num):
        self.hit = self.hit + num
    
    def getRBI(self):
        