import random
import entidades.Item as item
import copy

class Mapa:
    def __init__(self) -> None:
        
        # Inicializando cordenadas do lixo
        self.xLixo = 0
        self.yLixo = 0
        
        # Inicializando dicionário para armazenar cordenadas de todos os objetos no mapa
        self.cordenadas = {}

        # Inicializando dicionário para armazenar instâncias de itens
        self.itens = []
    
    def atualizarCordenadas(self, agente) -> None:
        """
        Atualiza as cordenadas de todos os objetos no dicionário
        """
        self.cordenadas = {}
        
        # Atualiza as cordenadas do agente
        self.cordenadas['agente'] = [agente.getX(), agente.getY()]
        # Atualiza as cordenadas do lixo
        self.cordenadas['lixo'] = [self.xLixo, self.yLixo]

        # Atualiza as cordenadas de cada item da lista
        for item in self.itens:
            self.cordenadas[f"{item.getRotulo()}"] = [item.getY(), item.getX(), item.getPeso()]
    
    def verificarCordenada(self, x, y) -> bool:
        """
        Verifica se a cordenada está disponível para ser ocupada
        """
        
        while (True):
            cordenadaDisponivel = True

            for indice, cordenada in enumerate(self.cordenadas.values()):
                if (x == cordenada[0] and y == cordenada[1]):
                    cordenadaDisponivel = False
                    break

            if (cordenadaDisponivel):
                return True
            else:
                return False

    def gerarItens(self, quantidade, peso) -> None:
        """
        Cria n itens com um determinado peso em cordenadas aleatórias
        """
        
        for i in range(quantidade):
            indiceItem = str(len(self.itens))
            while (True):
                # Calcular cordenadas
                x = random.randint(0, 19)
                y = random.randint(0, 19)

                # Validar cordenadas
                cordenadaDisponivel = self.verificarCordenada(x, y)

                if (cordenadaDisponivel == False):
                    self.atualizarMensagem(f"Cordenada indisponível em ({x}, {y}).")
                    continue
                else:
                    # Cria uma nova instancia de um item e adiciona à lista de itens
                    self.itens.append(item.Item(f"item_{indiceItem}", x, y, peso))
                    break

    def desenhar(self) -> str:
        """
        Função para gerar o mapa com os objetos nas localizações especificadas
        """
        mapa = ''
        # Variável temporária para guardar a localização dos objetos que serão renderizados na tela
        objetos = copy.deepcopy(self.cordenadas)
        # Variável temporária para guardar a chave do objeto encontrado no mapeamento
        chaveEncontrada = ''
        
        for x in range(20):
            for y in range(20):
                objetoEncontrado = False
                simbolo = '   '
                # Percorre o dicionário temporário de cordenadas ocupadas
                for chave in objetos:
                    # Verifica se as cordenadas da iteração atual correspondem às cordenadas do objeto
                    if (x == objetos[chave][0] and y == objetos[chave][1]):
                        objetoEncontrado = True
                        chaveEncontrada = chave
                        # Verifica o tipo de objeto
                        if (chave == 'agente'):  # Verifica se é tipo agente
                            simbolo = '[A]'
                        elif ('item' in chave):  # Verifica se é tipo item
                            peso = objetos[chave][2]
                            simbolo = f'[{peso}]'
                        elif (chave == 'lixo'):  # Verifica se é tipo lixo
                            simbolo = '[L]'

                    # Encerra o loop do dicionário ao encontrar as cordenadas correspondentes do objeto
                    if (objetoEncontrado == True):
                        # Deleta o objeto do dicionário temporário para otimizar o loop de busca
                        del objetos[chaveEncontrada]
                        break
                mapa = mapa + simbolo
            mapa = mapa + '\n'
        # Retorna o desenho do mapa
        return mapa

    # GETTERS
     
    def getItens(self) -> list:
        return self.itens
    
    def getCordenadas(self) -> dict:
        return self.cordenadas
        
    # SETTERS        

    def setCordenadasLixo(self, x, y) -> None:
        self.xLixo = x
        self.yLixo = y
        
    def setCordenadasAgente(self, agente, x, y) -> None:
        agente.setX(x)
        agente.setY(y)