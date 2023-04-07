from arquiteturas.IA import IA
from entidades.Agente import Agente

class Objetivo(IA):
    def __init__(self, agente: Agente) -> None:
        super().__init__(agente)
        
        self.localizarItemProximo = True
        self.xItemProximo = 0
        self.yItemProximo = 0
        self.proximoAlvo = None
            
    def executar(self, cordenadas: dict, itens: list) -> None:
        
        if self.agente.getEstado() == False and self.localizarItemProximo == True:
            # Verificar itens próximo
            item = self.percepcaoProximidade(cordenadas)
            self.xItemProximo = cordenadas[item][1]
            self.yItemProximo = cordenadas[item][0]
            self.localizarItemProximo = False
            self.proximoAlvo = [self.xItemProximo, self.yItemProximo]
        elif self.agente.getEstado() == False:
            # Verifica se o agente está em cima do item escolhido para coletar
            if (self.percepcaoItem(cordenadas) and self.verificarPosicaoItemAgente()):
                self.analisarItem(itens)
            self.deslocarAteCordenadas(self.xItemProximo, self.yItemProximo)
        else:
            # Caso o agente esteja com algum item, será deslocado para o lixo
            self.deslocarAteCordenadas(19, 19)
            self.localizarItemProximo = True
            
            # Verifica se o agente está em cima do lixo, caso estiver, irá soltar o item
            if self.percepcaoLixo(cordenadas):
                self.verificarEstado()
            
    def verificarPosicaoItemAgente(self) -> bool:
        """
        Verifica se a posição do agente coincide com a posição do item que está sendo procurado
        """
        if (self.getAgente().getX() == self.yItemProximo) and (self.getAgente().getY() == self.xItemProximo):
            return True
        
    def percepcaoProximidade(self, cordenadas: dict) -> str:
        """
        Verifica qual o item mais próximo da posição do agente
        """
        distancias = self.mapearDistancias(cordenadas)
        
        # Verificar o item mais próximo
        menorDistancia = 30
        itemProximo = ''
        for distancia in distancias:
            if distancias[distancia] < menorDistancia:
                menorDistancia = distancias[distancia]
                itemProximo = distancia
        
        return itemProximo
    
    def getProximoAlvo(self) -> list:
        return self.proximoAlvo