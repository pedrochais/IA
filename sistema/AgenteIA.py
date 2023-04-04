import random

class AgenteIA:
    def __init__(self, agente):
        # Instância do agente
        self.agente = agente
        
        # Guarda as cordenadas do deslocamento anterior
        self.yAnterior = 0
        self.xAnterior = 0
        
        self.itemEncontrado = ''
        self.itemCarregado = ''
        
        self.itensColetados = []
        
    #COMPORTAMENTOS DO AGENTE
    
    def deslocarAleatoriamente(self):
        """
        Comportamento em que a IA se desloca de forma aleatória pelo mapa
        """
        # Gera um numero inteiro aleatório para determinar o sentido do deslocamento
        sentido = random.randint(0, 3)

        # Antes de realizar um deslocamento o programa armazena as cordenadas anteriores do agente
        self.armazenarCordenadasAnteriores()
        
        # A nova localização do agente é calculada
        if(sentido == 0):
            self.agente.deslocarDireita()
        elif(sentido == 1):
            self.agente.deslocarEsquerda()
        elif(sentido == 2):
            self.agente.deslocarCima()
        elif(sentido == 3):
            self.agente.deslocarBaixo()
    
    def deslocarAteLixeira(self, xLixo, yLixo):
        # Antes de realizar um deslocamento o programa armazena as cordenadas anteriores do agente
        self.armazenarCordenadasAnteriores()
        
        if self.agente.getY() < xLixo:
            self.agente.deslocarDireita()
        elif self.agente.getY() > xLixo:
            self.agente.deslocarEsquerda()
        elif self.agente.getX() < yLixo:
            self.agente.deslocarBaixo()
        elif self.agente.getX() > yLixo:
            self.agente.deslocarCima()
            
    #SENSORES DO AGENTE
    
    def percepcaoLimitesDoMapa(self, x, y):
        # Verificar se o agente está dentro dos limites do mapa
        if (x > 19 or x < 0 or y > 19 or y < 0):
            # Se o a gente ultrapassou os limites do mapa ele volta para a cordenada anterior
            self.retornarParaCordenadaAnterior()
            return True
        else:
            return False
        
    def percepcaoCordenadas(self, cordenadas, itens):
        for rotulo in cordenadas:
            # Compara as cordenadas do agente com o objeto
            if(cordenadas[rotulo][0] == self.agente.getX() and cordenadas[rotulo][1] == self.agente.getY()):
                # Verifica se é tipo item e atribui o rótulo
                if ('item' in rotulo):
                    self.itemEncontrado = rotulo
                    self.analisarItem(itens)
                elif ('lixo' in rotulo):
                    self.verificarEstado()
                return True
        self.itemEncontrado = ''
    
    # DEMAIS FUNÇÕES
    
    def armazenarCordenadasAnteriores(self):
        self.xAnterior = self.agente.getX()
        self.yAnterior = self.agente.getY()
        
    def retornarParaCordenadaAnterior(self):
        xAtual = self.agente.getX()
        yAtual = self.agente.getY()
        
        # Verifica a diferença da cordenada atual com a cordenada anterior para determinar em qual eixo se deu o deslocamento
        if(self.xAnterior != xAtual):
            # Se o deslocamento se deu no eixo x o agente retorna para a cordenada x anterior
            self.agente.setX(self.xAnterior)
        elif(self.yAnterior != yAtual):
            # Se o deslocamento se deu no eixo y o agente retorna para a cordenada y anterior
            self.agente.setY(self.yAnterior)
    
    def analisarItem(self, itens):
        itemAtual = None
        
        # Buscar objeto item com o rótulo armazenado
        for item in itens:
            if item.getRotulo() == self.itemEncontrado:
                itemAtual = item
        
        # Caso o agente não estiver carregando algo
        if self.agente.getEstado() == False:
            self.itemCarregado = self.itemEncontrado
            self.agente.coletar(itemAtual)
            
            # Remove item da lista de itens no mapa após a coleta
            itens.remove(itemAtual)
        # Se o peso do item atualmente encontrado for maior que o peso do item que o agente já está carregando
        elif itemAtual.getPeso() > self.agente.getItem().getPeso():
                # Solta o item que estava carregando e coleta o item atual
                self.agente.soltar()
                # Insere o item no mapa que estava carregando no mapa
                itens.append(self.agente.getItem())
                # Coleta o item de maior peso
                self.itemCarregado = itemAtual.getRotulo()
                self.agente.coletar(itemAtual)
        else:
            pass
            
    def verificarEstado(self):
        # Verifica se o agente está carregando algum lixo
        if self.agente.getEstado() == True:
            self.agente.soltar()
            self.itensColetados.append(self.agente.getItem())
            self.itemCarregado = ''
        
    # GETTERS
    
    def getItensColetados(self):
        return self.itensColetados
    
    def getAgente(self):
        return self.agente
    
    def getXAnterior(self):
        return self.xAnterior
    
    def getYAnterior(self):
        return self.yAnterior