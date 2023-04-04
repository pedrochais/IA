import sistema.Mapa as mapa
import sistema.AgenteIA as agenteia
import sistema.App as app
import interface.UI as UI
import entidades.Agente as agente

agente = agente.Agente()
agenteIA = agenteia.AgenteIA(agente)
mapa = mapa.Mapa()
ui = UI.UI()

aplicativo = app.App(agenteIA, mapa, ui)

aplicativo.loop()