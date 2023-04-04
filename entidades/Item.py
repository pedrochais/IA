class Item:
    def __init__(self, rotulo, x, y, peso):
        self.rotulo = rotulo
        self.x = x
        self.y = y
        self.peso = peso

    def getRotulo(self):
        return self.rotulo

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, x):
        self.y = x

    def setY(self, y):
        self.x = y

    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso
