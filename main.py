import forca
import message


posicao = 1
quantidade_de_jogadores = message.pede_quantidade_de_jogadores()

#### Inicializa os jogadores ####
lista_de_jogadores= [0]*(quantidade_de_jogadores)


for i in range(quantidade_de_jogadores):
    nome = message.insere_nome(i)
    lista_de_jogadores[i] = forca.define_jogadores(nome.upper())

#### Executando o jogo ####
numero_maximo_jogadores = len(lista_de_jogadores)
id_jogador=0
continua = True
while continua:
    if(id_jogador == numero_maximo_jogadores):
        id_jogador=0    
    continua = forca.jogando(lista_de_jogadores,id_jogador,posicao)
    id_jogador = id_jogador+1


vencedores = 0

message.resultados(lista_de_jogadores)






