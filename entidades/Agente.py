class Agente:
    def __init__(self) -> None:
        self.y = 0
        self.x = 0
        self.carregado = False
        self.item = None
        
    def deslocarEsquerda(self) -> None:
        self.x = self.x - 1

    def deslocarDireita(self) -> None:
        self.x = self.x + 1

    def deslocarCima(self) -> None:
        self.y = self.y - 1

    def deslocarBaixo(self) -> None:
        self.y = self.y + 1

    def coletar(self, item) -> None:
        self.carregado = True
        self.item = item
        
    def soltar(self) -> None:
        self.carregado = False
        self.item.setX(self.x)
        self.item.setY(self.y)
        
    # GETTERS

    def getX(self) -> int:
        return self.y

    def getY(self) -> int:
        return self.x
    
    def getEstado(self) -> str:
        return self.carregado
    
    def getItem(self):
        return self.item
    
    # SETTERS
    
    def setX(self, x) -> None:
        self.y = x

    def setY(self, y) -> None:
        self.x = y