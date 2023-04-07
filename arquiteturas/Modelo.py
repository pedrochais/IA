from arquiteturas.IA import IA

class Modelo(IA):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        
        self.deslocarParaItem = False
        
    def executar(self, cordenadas, itens) -> None:
            
            if self.agente.getEstado() == False and self.deslocarParaItem == True:
                # Desloca-se até a cordenada do ultimo item coletado
                self.deslocarUltimaCordenadaItemColetado()
                
                x, y = self.getCordenadasItemColetado()
                
                # Quando chega até a cordenada do item que foi coletado volta para o deslocamento padrão
                if self.getAgente().getX() == y and self.getAgente().getY() == x:
                    self.deslocarParaItem = False
                    
            elif self.agente.getEstado() == False:
                # Deslocamento padrão da IA
                self.deslocarPadrao()
                
                if self.percepcaoItem(cordenadas):
                    self.analisarItem(itens)
            else:
                # Caso o agente esteja com algum item, será deslocado para o lixo
                self.deslocarAteCordenadas(19, 19)
                self.deslocarParaItem = True
                
                if self.percepcaoLixo(cordenadas):
                    self.verificarEstado()
                    
    def deslocarUltimaCordenadaItemColetado(self) -> None:
        self.deslocarAteCordenadas(self.xItemColetado, self.yItemColetado)
                    
            