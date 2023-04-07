import sistema.Mapa as map
import arquiteturas.Simples as iasimples
import arquiteturas.Modelo as iamodelo
import arquiteturas.Objetivo as iaobjetivo
import arquiteturas.Utilidade as iautilidade
import sistema.App as app
import interface.UI as UI
import entidades.Agente as ag

agente = ag.Agente()
mapa = map.Mapa()
ui = UI.UI()

arquitetura = 'utilidade'

if arquitetura == 'simples':
    ia = iasimples.Simples(agente)
elif arquitetura == 'modelo':
    ia = iamodelo.Modelo(agente)
elif arquitetura == 'objetivo':
    ia = iaobjetivo.Objetivo(agente)
elif arquitetura == 'utilidade':  
    ia = iautilidade.Utilidade(agente)
else:
    pass

aplicativo = app.App(ia, mapa, ui)

aplicativo.loop()