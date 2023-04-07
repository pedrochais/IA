import random
from entidades.Agente import Agente

class IA:
    def __init__(self, agente: Agente):
        # Instância do agente
        self.agente = agente
        
        self.itemEncontrado = ''
        self.itemCarregado = ''
        
        self.itensColetados = []
        
        # Sentidos dos deslocamentos do agente
        self.sentidoX = 'direita'
        self.sentidoY = 'baixo'
        
        # Guarda na memória do agente as cordenadas em que o item foi coletado
        self.xItemColetado = 0
        self.yItemColetado = 0
        
        # Guarda o item coletado
        self.itemAtual = None
        
    # COMPORTAMENTOS DO AGENTE
    
    def deslocarPadrao(self) -> None:
        """
        Comportamento em que a IA se desloca num padrão zigue-zague pelo mapa
        """

        # Antes de realizar um deslocamento o programa armazena as cordenadas anteriores do agente
        self.armazenarCordenadasAnteriores()
        
        # Verifica se o agente está em alguma das extremidades no eixo vertical do mapa
        if(self.agente.getX() == 0):
            self.sentidoY = 'baixo'
        elif(self.agente.getX() == 19):
            self.sentidoY = 'cima'
            
        # Verifica se o agente está em alguma das extremidades no eixo horizontal do mapa
        if(self.sentidoX == 'direita' and self.agente.getY() < 19):
            self.agente.deslocarDireita()
        elif(self.sentidoX == 'direita' and self.agente.getY() == 19):
            if self.sentidoY == 'cima':
                self.agente.deslocarCima()
            elif self.sentidoY == 'baixo':
                self.agente.deslocarBaixo()
            self.sentidoX = 'esquerda'
        elif(self.sentidoX == 'esquerda' and self.agente.getY() > 0):
            self.agente.deslocarEsquerda()
        elif(self.sentidoX == 'esquerda' and self.agente.getY() == 0):
            if self.sentidoY == 'cima':
                self.agente.deslocarCima()
            elif self.sentidoY == 'baixo':
                self.agente.deslocarBaixo()
            self.sentidoX = 'direita'

    def deslocarAteCordenadas(self, x: int, y: int) -> None:
        """
        Método para deslocar o agente até uma determinada cordenada x, y
        """
        # Antes de realizar um deslocamento o programa armazena as cordenadas anteriores do agente
        self.armazenarCordenadasAnteriores()
        
        if self.agente.getY() < x:
            self.agente.deslocarDireita()
        elif self.agente.getY() > x:
            self.agente.deslocarEsquerda()
        elif self.agente.getX() < y:
            self.agente.deslocarBaixo()
        elif self.agente.getX() > y:
            self.agente.deslocarCima()
            
    # SENSORES DO AGENTE
    
    def percepcaoItem(self, cordenadas: dict) -> bool:
        """
        Verifica se o agente encontrou algum item
        """
        for rotulo in cordenadas:
            # Verifica se o agente está em cima de um determinado objeto
            if(cordenadas[rotulo][0] == self.agente.getX() and cordenadas[rotulo][1] == self.agente.getY()):
                # Verifica se é o objeto é tipo item e atribui o rótulo
                if ('item' in rotulo):
                    self.itemEncontrado = rotulo
                    return True
                
        self.itemEncontrado = ''
        
    def percepcaoLixo(self, cordenadas: dict) -> bool:
        """
        Verifica se o agente encontrou o lixo
        """
        for rotulo in cordenadas:
            # Verifica se o agente está em cima de um determinado objeto
            if(cordenadas[rotulo][0] == self.agente.getX() and cordenadas[rotulo][1] == self.agente.getY()):
                # Verifica se é o objeto é tipo lixo
                if ('lixo' in rotulo):
                    self.verificarEstado()
                    return True
    
    # DEMAIS FUNÇÕES
    
    def armazenarCordenadasAnteriores(self) -> None:
        self.xAnterior = self.agente.getX()
        self.yAnterior = self.agente.getY()

    def analisarItem(self, itens: list) -> None:
        """
        Verifica se o objeto sobre o qual o agente está é um item, caso sim, coleta-o
        """
    
        # Buscar objeto item com o rótulo armazenado
        for item in itens:
            if item.getRotulo() == self.itemEncontrado:
                self.itemAtual = item
        
        # Caso o agente não estiver carregando algo
        if self.agente.getEstado() == False:
            self.itemCarregado = self.itemEncontrado
            self.agente.coletar(self.itemAtual)
            
            # Remove item da lista de itens no mapa após a coleta
            itens.remove(self.itemAtual)
            
    def verificarEstado(self) -> None:
        """
        Caso o agente estiver sobre a lixeira, solta o item que está carregando
        """
        # Verifica se o agente está carregando algum lixo
        if self.agente.getEstado() == True:
            self.agente.soltar()
            self.itensColetados.append(self.agente.getItem())
            self.itemCarregado = ''
        
    def mapearDistancias(self, cordenadas: dict) -> dict:
        """
        Calcula a distância do agente em relação a todos os itens do mapa
        """
        x = self.agente.getX()
        y = self.agente.getY()
        
        distancias = {}
        
        for cordenada in cordenadas:
            # Verifica se o objeto é um item
            if 'item' in cordenada:
                # Calcula a distância do agente até o objeto
                distancia = ((x - cordenadas[cordenada][0])**2 + (y - cordenadas[cordenada][1])**2)**0.5
                distancias[cordenada] = distancia
        
        return distancias
        
    # GETTERS
    
    def getItensColetados(self) -> list:
        return self.itensColetados
    
    def getItensReciclaveis(self) -> list:
        itensReciclaveis = []
        
        for item in self.itensColetados:
            if item.getPeso() == 5:
                itensReciclaveis.append(item)
                
        return itensReciclaveis
    
    def getItensOrganicos(self) -> list:
        itensOrganicos = []
        
        for item in self.itensColetados:
            if item.getPeso() == 1:
                itensOrganicos.append(item)
                
        return itensOrganicos

    def getCordenadasItemColetado(self) -> int:
        return self.xItemColetado, self.yItemColetado
    
    def getAgente(self) -> Agente:
        return self.agente
    
    def getXAnterior(self) -> int:
        return self.xAnterior
    
    def getYAnterior(self) -> int:
        return self.yAnterior