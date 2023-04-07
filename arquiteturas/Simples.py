from arquiteturas.IA import IA
from entidades.Agente import Agente

class Simples(IA):
    def __init__(self, agente: Agente) -> None:
        super().__init__(agente)
        
    def executar(self, cordenadas: dict, itens: list) -> None:
        
        if self.agente.getEstado() == False:
            # Deslocamento padrão da IA
            self.deslocarPadrao()
            
            # Verifica se o agente está em cima do item
            if self.percepcaoItem(cordenadas):
                self.analisarItem(itens)
                
        else:
            # Caso o agente esteja com algum item, será deslocado para o lixo
            self.deslocarAteCordenadas(19, 19)
            
            # Verifica se o agente está em cima do lixo, caso estiver, irá soltar o item
            if self.percepcaoLixo(cordenadas):
                self.verificarEstado()
        
        