from arquiteturas.IA import IA

class Utilidade(IA):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        
        self.localizarItemMaiorPeso = True
        
    def executar(self, cordenadas, itens) -> None:
        if self.agente.getEstado() == False and self.localizarItemMaiorPeso == True:
            # Verificar itens próximo
            item = self.percepcaoTipo(cordenadas)
            self.xItemProximo = cordenadas[item][1]
            self.yItemProximo = cordenadas[item][0]
            self.localizarItemMaiorPeso = False
        elif self.agente.getEstado() == False:
            # Verifica se o agente está em cima do item
            if (self.percepcaoItem(cordenadas) and self.verificarPosicaoItemAgente()):
                self.analisarItem(itens)
            self.deslocarAteCordenadas(self.xItemProximo, self.yItemProximo) 
        else:
            # Caso o agente esteja com algum item, será deslocado para o lixo
            self.deslocarAteCordenadas(19, 19)
            self.localizarItemMaiorPeso = True
            
            if self.percepcaoLixo(cordenadas):
                self.verificarEstado()
            
    def verificarPosicaoItemAgente(self) -> bool:
        """
        Verifica se a posição do agente coincide com a posição do item que está sendo procurado
        """
        if (self.getAgente().getX() == self.yItemProximo) and (self.getAgente().getY() == self.xItemProximo):
            return True
        
    def percepcaoTipo(self, cordenadas) -> bool:
        """
        Verifica qual o item mais próximo da posição do agente
        """
        distanciasOrdenado = {}
        itensOrdenados = []
        
        distancias = self.mapearDistancias(cordenadas)
        
        # Ordenando dicionário com base nas distâncias
        for rotulo in sorted(distancias, key = distancias.get):
            distanciasOrdenado[rotulo] = distancias[rotulo]
        
        for rotulo in distanciasOrdenado:
            if cordenadas[rotulo][2] == 5:
                itensOrdenados.append(rotulo)
                
        for rotulo in distanciasOrdenado:
            if cordenadas[rotulo][2] == 1:
                itensOrdenados.append(rotulo)

        itemProximo = itensOrdenados[0]

        return itemProximo