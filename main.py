# Jogo da Forca - Trabalho final do segundo módulo da Trilha Resília - Dezembro de 2021
# Equipe: Luana, Nathalia, Ronaldo Paraski e Vitor Hugo
# Módulo: Main - Módulo responsável por "dar o pontapé inicial" ao jogo, controlando o fluxo entre demais módulos
################################################################################################################

import forca
import message

#Inicialização do jogo
message.instrucoes()
quantidade_de_jogadores = message.pede_quantidade_de_jogadores()

lista_de_jogadores= [0]*(quantidade_de_jogadores)
palavras_ja_sorteadas=[""]

#Cria Jogadores
for i in range(quantidade_de_jogadores):
    nome = message.insere_nome(i)
    lista_de_jogadores[i] = forca.define_jogadores(nome.upper(),palavras_ja_sorteadas)



#Multiplayer 
numero_maximo_jogadores = len(lista_de_jogadores)
id_jogador=0
continua = True
while continua:
    if(id_jogador == numero_maximo_jogadores):
        id_jogador=0    
    continua = forca.jogando(lista_de_jogadores,id_jogador) #chama o jogo
    id_jogador = id_jogador+1


#Ranking
vencedores = 0
message.resultados(lista_de_jogadores)

