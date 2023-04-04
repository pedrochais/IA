class Agente:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.carregado = False
        self.item = None
        
    def deslocarEsquerda(self):
        self.x = self.x - 1

    def deslocarDireita(self):
        self.x = self.x + 1

    def deslocarCima(self):
        self.y = self.y - 1

    def deslocarBaixo(self):
        self.y = self.y + 1

    def coletar(self, item):
        self.carregado = True
        self.item = item
        
    def soltar(self):
        self.carregado = False
        self.item.setX(self.x)
        self.item.setY(self.y)
        
    # GETTERS

    def getX(self):
        return self.y

    def getY(self):
        return self.x
    
    def getEstado(self):
        return self.carregado
    
    def getItem(self):
        return self.item
    
    # SETTERS
    
    def setX(self, x):
        self.y = x

    def setY(self, y):
        self.x = y