class UI:
    def __init__(self) -> None:
        self.cabecalhoMensagem = ''
        self.mensagem = ''
        
        self.loopAtual = 0
        self.xAtualAgente = 0
        self.yAtualAgente = 0
        self.reciclaveisColetados = 0
        self.organicosColetados = 0
        self.proximoAlvo = None

    def renderizar(self, mapa: str) -> None:
        """
        Renderizar os componentes gráficos na tela
        """
        # Mensagem com informações do programa
        print(self.cabecalhoMensagem)
        # Mensagem disparada por evento
        print(self.mensagem)
        # Desenho do mapa
        print("╭────────────────────────────╯•╰────────────────────────────╮")
        print(mapa, end="")
        print("╰────────────────────────────╮•╭────────────────────────────╯")
        
    def atualizarCabecalhoMensagem(self, loopAtual: int, xAtualAgente: int, yAtualAgente: int, reciclaveisColetados: int, organicosColetados: int, proximoAlvo: list) -> None:
        self.loopAtual = loopAtual
        self.xAtualAgente = xAtualAgente
        self.yAtualAgente = yAtualAgente
        self.reciclaveisColetados = reciclaveisColetados
        self.organicosColetados = organicosColetados
        self.proximoAlvo = proximoAlvo
        
        self.cabecalhoMensagem = f"""↻  Loop: {loopAtual}
⛉  Agente: ({xAtualAgente}, {yAtualAgente})
♻  Recicláveis coletados: {reciclaveisColetados}
⛬  Orgânicos coletados: {organicosColetados}
☑  Pontos: {organicosColetados*1 + reciclaveisColetados*5}"""

        if self.proximoAlvo != None:
            self.cabecalhoMensagem = self.cabecalhoMensagem + f"\n☒  Próximo alvo: {self.proximoAlvo[0], self.proximoAlvo[1]}"

    def atualizarMensagem(self, loopAtual: int, mensagem: str) -> None:
        self.mensagem = f'[{loopAtual}] {mensagem}'
        
    def fim(self, loopAtual: int) -> None:
        print(f"[{loopAtual}] Todos os itens foram coletados!")