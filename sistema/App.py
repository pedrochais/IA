from time import sleep
from arquiteturas.IA import IA
from arquiteturas.Utilidade import Utilidade
from arquiteturas.Objetivo import Objetivo
from interface.UI import UI

class App:
    def __init__(self, arquiteturaIA: IA, mapa: str, UI: UI) -> None:
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
            sleep(.05)
            print("\x1b[2J")
            # Volta para a posição inicial do scroll 
            print("\x1b[0;0f")
            
            # Atualizar a nova localização dos objetos no dicionario
            self.mapa.atualizarCordenadas(self.agente)
            
            # Verifica os dados da mensagem de cabeçalho e salva na UI
            self.atualizarDados()
            
            # Renderizar o mapa com os objetos
            self.UI.renderizar(self.mapa.desenhar())
            
            if len(self.arquiteturaIA.getItensColetados()) == 15:
                self.UI.fim(self.loopAtual)
                input()
            
            # Verificar sensores e executar ações do agente
            self.atualizarIA()
            
    def configuracoesIniciais(self) -> None:
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
    
    def atualizarLoopAtual(self) -> None:
        """
        Incrementa o contador de loops
        """
        self.loopAtual = self.loopAtual + 1
    
    def atualizarMensagem(self, mensagem: str) -> None:
        """
        Atualiza a mensagem provocada por algum evento na UI
        """
        self.UI.atualizarMensagem(self.loopAtual, mensagem)
            
    def atualizarDados(self) -> None:
        """
        Atualiza a mensagem com informações do programa na UI
        """
        self.atualizarLoopAtual()
        if isinstance(self.arquiteturaIA, Utilidade) or isinstance(self.arquiteturaIA, Objetivo):
            self.UI.atualizarCabecalhoMensagem(self.loopAtual, 
                                               self.agente.getY(), 
                                               self.agente.getX(), 
                                               len(self.arquiteturaIA.getItensReciclaveis()), 
                                               len(self.arquiteturaIA.getItensOrganicos()), 
                                               self.arquiteturaIA.getProximoAlvo())
        else:
            self.UI.atualizarCabecalhoMensagem(self.loopAtual, 
                                               self.agente.getY(), 
                                               self.agente.getX(), 
                                               len(self.arquiteturaIA.getItensReciclaveis()), 
                                               len(self.arquiteturaIA.getItensOrganicos()), 
                                               None)
        
    def atualizarIA(self) -> None:
        self.arquiteturaIA.executar(self.mapa.getCordenadas(), self.mapa.getItens())