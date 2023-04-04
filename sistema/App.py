from time import sleep

class App:
    def __init__(self, agenteIA, mapa, UI):
        self.agenteIA = agenteIA
        self.agente = agenteIA.getAgente()
        self.mapa = mapa
        self.UI = UI
        
        # Inicializando variável de controle para contabilizar os loops do programa
        self.loopAtual = 0
        
    def loop(self):
        self.configuracoesIniciais()
        
        while(True):
            # Intervalo entre cada loop
            sleep(.1)
            print("\x1b[2J")
            # Volta para a posição inicial do scroll 
            print("\x1b[0;0f")
            
            if len(self.agenteIA.getItensColetados()) == 15:
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
            

    def configuracoesIniciais(self):
        """
        Carrega as configurações iniciais do mapa
        """
        
        # Gerando instâncias e calculando cordenadas para lixos orgânicos
        self.mapa.gerarItens(10, 1)
        # Gerando instâncias e calculando cordenadas para lixos recicláveis
        self.mapa.gerarItens(5, 5)
        # Calculando cordenadas para para o lixo
        self.mapa.setCordenadasLixo(19, 19)
        # Calculando cordenadas para o agente
        self.mapa.setCordenadasAgente(self.agente, 0, 0)
    
    def atualizarLoopAtual(self):
        """
        Incrementa o contador de loops
        """
        self.loopAtual = self.loopAtual + 1
    
    def atualizarMensagem(self, mensagem):
        """
        Atualiza a mensagem provocada por algum evento na UI
        """
        self.UI.atualizarMensagem(self.loopAtual, mensagem)
            
    def atualizarDados(self):
        """
        Atualiza a mensagem com informações do programa na UI
        """
        self.atualizarLoopAtual()
        self.UI.atualizarCabecalhoMensagem(self.loopAtual, self.agente.getY(), self.agente.getX(), len(self.agenteIA.getItensColetados()))
        
    def atualizarIA(self):
        """
        Método para atualizar o comportamento da IA e fazer todas as validações necessárias de acordo com as suas percepções
        """
        # Ação do agente
        if self.agente.getEstado() == False:
            self.agenteIA.deslocarAleatoriamente()
        else:
            self.agenteIA.deslocarAteLixeira(19, 19)
        
        # Recupera as cordenadas do agente após o deslocamento
        x = self.agenteIA.getAgente().getX()
        y = self.agenteIA.getAgente().getY()
         
        # Percepção de objetos interativos no mapa
        encontrouObjeto = self.agenteIA.percepcaoCordenadas(self.mapa.getCordenadas(), self.mapa.getItens())
    
        # Percepção de limites do mapa
        ultrapassouLimite = self.agenteIA.percepcaoLimitesDoMapa(x, y)
        
        # Condicional para atualizar a mensagem que será apresentada na UI
        if(encontrouObjeto):
            #self.agenteIA.verificarItem(self.localizacaoObjetosInterativos)
            self.atualizarMensagem(f"Objeto encontrado em ({y}, {x}).")
        
        # Condicional para atualizar a mensagem que será apresentada na UI
        if(ultrapassouLimite):
            # Recupera as cordenadas anteriores do agente
            xAnterior = self.agenteIA.getXAnterior()
            yAnterior = self.agenteIA.getYAnterior()
            
            self.atualizarMensagem(f"Limite do mapa ultrapassado em ({y}, {x}), retornando para ({yAnterior}, {xAnterior}).")
        