from arquiteturas.IA import IA

class Objetivo(IA):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        
        self.localizarItemProximo = True
        self.xItemProximo = 0
        self.yItemProximo = 0
            
    def executar(self, cordenadas, itens) -> None:
        
        if self.agente.getEstado() == False and self.localizarItemProximo == True:
            # Verificar itens próximo
            item = self.percepcaoProximidade(cordenadas)
            self.xItemProximo = cordenadas[item][1]
            self.yItemProximo = cordenadas[item][0]
            self.localizarItemProximo = False
        elif self.agente.getEstado() == False:
            if (self.percepcaoItem(cordenadas) and self.verificarPosicaoItemAgente()):
                self.analisarItem(itens)
            self.deslocarAteCordenadas(self.xItemProximo, self.yItemProximo)
        else:
            # Caso o agente esteja com algum item, será deslocado para o lixo
            self.deslocarAteCordenadas(19, 19)
            self.localizarItemProximo = True
            
            if self.percepcaoLixo(cordenadas):
                self.verificarEstado()
            
    def verificarPosicaoItemAgente(self) -> bool:
        """
        Verifica se a posição do agente coincide com a posição do item que está sendo procurado
        """
        if (self.getAgente().getX() == self.yItemProximo) and (self.getAgente().getY() == self.xItemProximo):
            return True
        
    def percepcaoProximidade(self, cordenadas) -> str:
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