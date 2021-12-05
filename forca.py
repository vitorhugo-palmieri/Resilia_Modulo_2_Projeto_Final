import random
import message

def define_jogadores(nome):
        
        return {
            "nome":nome,
            "letras_acertadas":[],
            "letras_erradas":[],
            "palavra_do_jogo":carrega_palavras_secreta(),
            "palavras_jogadas":[]

        }

def jogando(lista_de_jogadores,id_jogador):

    enforcou = False
    acertou = False
    erros = 0
    errou_letra = False
    jogador_atual = lista_de_jogadores[id_jogador]

    while (not enforcou and not acertou and not errou_letra):
        message.intro_jogador(jogador_atual)
        palavra_secreta = jogador_atual["palavra_do_jogo"]
        
        letras_acertadas = jogador_atual["letras_acertadas"]=inicializa_letras_acertadas(jogador_atual)
        print(letras_acertadas)
        
        chute=message.pede_chute()
        if len(chute)>1:
            decisao=message.pergunta_chute()
            if decisao:
                if (chute==jogador_atual["palavra_do_jogo"]):
                    continua = False
                    acertou = True
                else:
                    continua = False
                    enforcou =True
            else:
                chute=message.pede_chute
        else:
            if(chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas,palavra_secreta,jogador_atual)
                message.acertou_letra(chute)     
            else:
                erros = erros+1
                message.errou_letra()
                errou_letra = True
            continua=True
            acertou = "_" not in letras_acertadas
            enforcou = erros == 7     
        
    if acertou:
        message.ganhou_jogo(jogador_atual)
        continua=False  
    elif(enforcou):
        message.perdeu_jogo()
        continua=False
    
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






