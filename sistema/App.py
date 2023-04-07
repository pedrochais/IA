from time import sleep

class App:
    def __init__(self, arquiteturaIA, mapa, UI) -> None:
        self.arquiteturaIA = arquiteturaIA
        self.agente = arquiteturaIA.getAgente()
        self.mapa = mapa
        self.UI = UI
        
        # Inicializando variável de controle para contabilizar os loops do programa
        self.loopAtual = 0
        
    def loop(self) -> None:
        self.configuracoesIniciais()
        
        while(True):
            # Intervalo entre cada loop
            sleep(.10)
            print("\x1b[2J")
            # Volta para a posição inicial do scroll 
            print("\x1b[0;0f")
            
            if len(self.arquiteturaIA.getItensColetados()) == 10:
                self.UI.fim(self.loopAtual)
                input()
            
            # Atualizar a nova localização dos objetos no dicionario
            self.mapa.atualizarCordenadas(self.agente)
            
            # Verifica os dados da mensagem de cabeçalho e salva na UI
            self.atualizarDados()
            
            # Renderizar o mapa com os objetos
            self.UI.renderizar(self.mapa.desenhar())
            
            # Verificar sensores e executar ações do agente
            self.atualizarIA()
            
    def configuracoesIniciais(self) -> None:
        """
        Carrega as configurações iniciais do mapa
        """
        # Gerando instâncias e calculando cordenadas para lixos orgânicos
        self.mapa.gerarItens(5, 1)
        # Gerando instâncias e calculando cordenadas para lixos recicláveis
        self.mapa.gerarItens(5, 5)
        # Calculando cordenadas para para o lixo
        self.mapa.setCordenadasLixo(19, 19)
        # Calculando cordenadas para o agente
        self.mapa.setCordenadasAgente(self.agente, 0, 0)
    
    def atualizarLoopAtual(self) -> None:
        """
        Incrementa o contador de loops
        """
        self.loopAtual = self.loopAtual + 1
    
    def atualizarMensagem(self, mensagem) -> None:
        """
        Atualiza a mensagem provocada por algum evento na UI
        """
        self.UI.atualizarMensagem(self.loopAtual, mensagem)
            
    def atualizarDados(self) -> None:
        """
        Atualiza a mensagem com informações do programa na UI
        """
        self.atualizarLoopAtual()
        self.UI.atualizarCabecalhoMensagem(self.loopAtual, self.agente.getY(), self.agente.getX(), len(self.arquiteturaIA.getItensColetados()))
        
    def atualizarIA(self) -> None:
        self.arquiteturaIA.executar(self.mapa.getCordenadas(), self.mapa.getItens())
        self.atualizarPercepcoes()
        
        #print(self.agente.getEstado())
        #print(f"Agente X: {self.arquiteturaIA.getAgente().getX()}\nAgente Y: {self.arquiteturaIA.getAgente().getY()}\n\nItem X: {self.yItemProximo}\nItem Y: {self.xItemProximo}")
        
    def atualizarPercepcoes(self):
        """
        # Recupera as cordenadas do agente após o deslocamento
        x = self.arquiteturaIA.getAgente().getX()
        y = self.arquiteturaIA.getAgente().getY()
         
        # Percepção de objetos interativos no mapa (Coleta através do método 'percepcaoCordenadas')
        # encontrouObjeto = self.arquiteturaIA.percepcaoCordenadas(self.mapa.getCordenadas())
        
        #if (self.arquiteturaIA.getAgente().getX() == self.yItemProximo and self.arquiteturaIA.getAgente().getY() == self.xItemProximo) or (self.arquiteturaIA.getAgente().getX() == 19 and self.arquiteturaIA.getAgente().getY() == 19):
                #self.arquiteturaIA.percepcaoCordenadas(self.mapa.getCordenadas(), self.mapa.getItens())
    
        # Percepção de limites do mapa
        #ultrapassouLimite = self.arquiteturaIA.percepcaoLimitesDoMapa(x, y)
        
        # Condicional para atualizar a mensagem que será apresentada na UI
        #if(encontrouObjeto):
            #self.arquiteturaIA.verificarItem(self.localizacaoObjetosInterativos)
        #    self.atualizarMensagem(f"Objeto encontrado em ({y}, {x}).")
        
        # Condicional para atualizar a mensagem que será apresentada na UI
        if(ultrapassouLimite):
            # Recupera as cordenadas anteriores do agente
            xAnterior = self.arquiteturaIA.getXAnterior()
            yAnterior = self.arquiteturaIA.getYAnterior()
            
            self.atualizarMensagem(f"Limite do mapa ultrapassado em ({y}, {x}), retornando para ({yAnterior}, {xAnterior}).")
        """