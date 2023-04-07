import random

class IA:
    def __init__(self, agente):
        # Instância do agente
        self.agente = agente
        
        # Guarda as cordenadas do deslocamento anterior
        self.yAnterior = 0
        self.xAnterior = 0
        
        self.itemEncontrado = ''
        self.itemCarregado = ''
        
        self.itensColetados = []
        
        # Sentidos dos deslocamentos do agente
        self.sentidoX = 'direita'
        self.sentidoY = 'baixo'
        
        # Guarda na memória do agente as cordenadas em que o item foi coletado
        self.xItemColetado = 0
        self.yItemColetado = 0
        
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

    def deslocarAteCordenadas(self, x, y) -> None:
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
            
    #SENSORES DO AGENTE
    """
    def percepcaoLimitesDoMapa(self, x, y) -> bool:
        
        Verifica se o agente está dentro dos limites do mapa
       
        if (x > 19 or x < 0 or y > 19 or y < 0):
            # Se o a gente ultrapassou os limites do mapa ele volta para a cordenada anterior
            self.retornarParaCordenadaAnterior()
            return True
        else:
            return False
    """ 
    def percepcaoItem(self, cordenadas) -> bool:
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
        
    def percepcaoLixo(self, cordenadas) -> bool:
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
        
    def armazenarCordenadasItemColetado(self, x, y) -> None:
        self.xItemColetado = x
        self.yItemColetado = y
        
    def retornarParaCordenadaAnterior(self) -> None:
        xAtual = self.agente.getX()
        yAtual = self.agente.getY()
        
        # Verifica a diferença da cordenada atual com a cordenada anterior para determinar em qual eixo se deu o deslocamento
        if(self.xAnterior != xAtual):
            # Se o deslocamento se deu no eixo x o agente retorna para a cordenada x anterior
            self.agente.setX(self.xAnterior)
        elif(self.yAnterior != yAtual):
            # Se o deslocamento se deu no eixo y o agente retorna para a cordenada y anterior
            self.agente.setY(self.yAnterior)
    
    def analisarItem(self, itens) -> None:
        """
        Verifica se o objeto sobre o qual o agente está é um item, caso sim, coleta-o
        """
        itemAtual = None
        
        # Buscar objeto item com o rótulo armazenado
        for item in itens:
            if item.getRotulo() == self.itemEncontrado:
                itemAtual = item
        
        # Caso o agente não estiver carregando algo
        if self.agente.getEstado() == False:
            self.itemCarregado = self.itemEncontrado
            self.agente.coletar(itemAtual)
            self.armazenarCordenadasItemColetado(itemAtual.getX(), itemAtual.getY())
            
            # Remove item da lista de itens no mapa após a coleta
            itens.remove(itemAtual)
            
    def verificarEstado(self) -> None:
        """
        Caso o agente estiver sobre a lixeira, solta o item que está carregando
        """
        # Verifica se o agente está carregando algum lixo
        if self.agente.getEstado() == True:
            self.agente.soltar()
            self.itensColetados.append(self.agente.getItem())
            self.itemCarregado = ''
        
    def mapearDistancias(self, cordenadas) -> dict:
        x = self.agente.getX()
        y = self.agente.getY()
        
        distancias = {}
        
        # Mapear a distancia de todos os itens em relação ao agente
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
    
    def getAgente(self):
        return self.agente
    
    def getXAnterior(self) -> int:
        return self.xAnterior
    
    def getYAnterior(self) -> int:
        return self.yAnterior
    
    def getCordenadasItemColetado(self) -> int:
        return self.xItemColetado, self.yItemColetado
    