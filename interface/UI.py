class UI:
    def __init__(self):
        self.cabecalhoMensagem = ''
        self.mensagem = ''

    def renderizar(self, mapa):
        """
        Renderizar os componentes gráficos na tela
        """
        # Mensagem com informações do programa
        print(self.cabecalhoMensagem)
        # Mensagem disparada por evento
        print(self.mensagem)
        # Desenho do mapa
        print(mapa, end="")
        
    def atualizarCabecalhoMensagem(self, loopAtual, xAtualAgente, yAtualAgente, itensColetados):
        self.cabecalhoMensagem = f'Loop: {loopAtual} | Agente: ({xAtualAgente}, {yAtualAgente}) | Itens coletados: {itensColetados}'

    def atualizarMensagem(self, loopAtual, mensagem):
        self.mensagem = f'[{loopAtual}] {mensagem}'
        
    def fim(self, loopAtual):
        print(f"[{loopAtual}] Todos os itens foram coletados!")