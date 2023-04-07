from arquiteturas.IA import IA

class Simples(IA):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        
    def executar(self, cordenadas, itens) -> None:
        
        if self.agente.getEstado() == False:
            # Deslocamento padrão da IA
            self.deslocarPadrao()
        else:
            # Caso o agente esteja com algum item, será deslocado para o lixo
            self.deslocarAteCordenadas(19, 19)
            
            if self.percepcaoLixo(cordenadas):
                self.verificarEstado()
            
        
        if self.percepcaoItem(cordenadas):
            self.analisarItem(itens)