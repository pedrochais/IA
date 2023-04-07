class Item:
    def __init__(self, rotulo, x, y, peso) -> None:
        self.rotulo = rotulo
        self.x = x
        self.y = y
        self.peso = peso

    def getRotulo(self) -> str:
        return self.rotulo

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y
    
    def setX(self, x) -> None:
        self.y = x

    def setY(self, y) -> None:
        self.x = y

    def getPeso(self) -> int:
        return self.peso
    
    def setPeso(self, peso) -> None:
        self.peso = peso
