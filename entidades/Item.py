class Item:
    def __init__(self, rotulo: str, x: int, y: int, peso: int) -> None:
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
    
    def setX(self, x: int) -> None:
        self.y = x

    def setY(self, y: int) -> None:
        self.x = y

    def getPeso(self) -> int:
        return self.peso
    
    def setPeso(self, peso: int) -> None:
        self.peso = peso
