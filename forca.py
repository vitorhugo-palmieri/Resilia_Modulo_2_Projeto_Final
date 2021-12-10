import random
import message

def define_jogadores(nome):
        
        return {
            "nome":nome,
            "letras_acertadas":[],
            "letras_erradas":[],
            "palavra_do_jogo":carrega_palavras_secreta(),
            "perdeu":False,
            "ganhou":False,
            "pontos":100,
            "posicao": ""

        }

def verifica_perdedores(lista_jogadores):
    jogando = 0
    total_jogadores = len(lista_jogadores)
    for jogador in lista_jogadores:
        if not jogador["ganhou"] and not jogador["perdeu"]:
            jogando = jogando+1
    if jogando == 0:
        return False
    else: return True
    
def jogando(lista_de_jogadores,id_jogador,posicao):
    jogador_atual = lista_de_jogadores[id_jogador]
    

    continua = verifica_perdedores(lista_de_jogadores)

    if not jogador_atual["perdeu"] and not jogador_atual["ganhou"] :
        enforcou = False
        acertou = False
        total_tentativas = 7
        errou_letra = False
        
        while (not enforcou and not acertou and not errou_letra):
            palavra_secreta = jogador_atual["palavra_do_jogo"]
            pontos = jogador_atual["pontos"]
            letras_erradas = jogador_atual["letras_erradas"]

            letras_acertadas = jogador_atual["letras_acertadas"]=inicializa_letras_acertadas(jogador_atual)

            message.display_jogador(jogador_atual,total_tentativas)
            
            
            chute=message.pede_chute()
            #verifica se o usuario quer chutar a palavra toda
            if len(chute)>1:
                decisao=message.pergunta_chute()
                if decisao:
                    if (chute==jogador_atual["palavra_do_jogo"]):
                        acertou = True
                        
                    else:
                        enforcou =True
                        jogador_atual["pontos"] = 0

                else:
                    chute=message.pede_chute
            else:
                if (chute in letras_acertadas) or (chute in letras_erradas):
                    message.letra_chute_repetida()
                else :
                    if(chute in palavra_secreta):
                        marca_chute_correto(chute, letras_acertadas,palavra_secreta,jogador_atual)
                        message.acertou_letra(chute)     
                    else:
                        message.errou_letra(jogador_atual,chute)
                        jogador_atual["pontos"] = pontos - 10
                        errou_letra = True
                    
                    #condiçoes para ganhar ou perder
                    continua=True
                    acertou = "_" not in letras_acertadas
                    if len(jogador_atual["letras_erradas"])==total_tentativas:
                        enforcou = True
                     
            
        if acertou:
            message.acertou_palavra(jogador_atual)
            jogador_atual["ganhou"] = True
            jogador_atual["posicao"] = posicao 
            posicao = posicao + 1
        elif(enforcou):
            message.perdeu_jogo()
            jogador_atual["perdeu"] = True
        
    return continua

def carrega_palavras_secreta():
    arquivo=open("palavra.txt","r")
    palavras=[]
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero=random.randrange(0,len(palavras))
    palavra_secreta=palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(jogador_atual):
    if(len(jogador_atual["letras_acertadas"])==0):
        return ["_" for letra in jogador_atual["palavra_do_jogo"]]
    else:
        return jogador_atual["letras_acertadas"]

def marca_chute_correto(chute, letras_acertadas,palavra,jogador_atual):
    index=0
    index2=0
    for letra in palavra:
        if(chute==letra):
            letras_acertadas[index]=letra
        index=index+1
    for i in range(len(letras_acertadas)):
        jogador_atual["letras_acertadas"][i]=letras_acertadas[i]






