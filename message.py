
import time
import os

# def intro_jogador(jogador_atual):
    

def acertou_letra(chute):
    os.system("cls")
    print("\n\n\nACERTOU, TEM A LETRA {} NA PALAVRA".format(chute))
    time.sleep(2)
    os.system("cls")

def display_jogador(jogador_atual,total_tentativas, errado):
    
    palavra = jogador_atual["letras_acertadas"]
    letras_erradas=jogador_atual["letras_erradas"]
    os.system("cls")
    print("-------------------------------")
    print(f"   Jogando com {jogador_atual['nome']}")
    print("-------------------------------")
    print(f"\nA PALAVRA TEM {len(jogador_atual['palavra_do_jogo'])} LETRAS\n")
    time.sleep(1)
    

    forca = """
    ______
          | 
          |
          _
    """
    vazio = """ 


    """
    morreu ="""
        morreu
    """
    cabeca ="""
          O
    """
    tronco = """
          O
          |
    """
    braco_esquerdo = """
          O
         /|
    """
    braco_direito = """
          O
         /|\\
    """
    perna_esquerda = """
          O
         /|\\
         /
    """
    perna_direita = """
          O
         /|\\
         / \\
    """
    chances_boneco = [morreu, perna_direita, perna_esquerda, braco_direito, braco_esquerdo, tronco, cabeca, vazio]
    
    
    print(jogador_atual["dica"])
    print("LETRAS ERRADAS:",end=" ")
    for le in letras_erradas:
        print(le,end=" ")
    print(f"\nTENTATIVAS: {total_tentativas-len(jogador_atual['letras_erradas'])}")
    if errado >= 0:
        errado = errado-len(jogador_atual['letras_erradas'])
        print(forca+chances_boneco[errado])
    for l in palavra:
        print(l,end=" ")
    print("\n")  
    
    
    # print("-------------------------------------------------------------------------------")


def letra_chute_repetida():
    # time.sleep(2)
    os.system("cls")
    print("\n\n\nVOCÊ JÁ CHUTOU ESSA LETRA, ESCOLHA OUTRA")
    time.sleep(1.5)
    os.system("cls")

def errou_letra(jogador,chute):
   
    os.system("cls")
    print(f"\n\n\nNÃO TEM {chute} NA PALAVRA")

    time.sleep(2)
    os.system("cls")
    jogador['letras_erradas'].append(chute)

def instrucoes():
    os.system("cls")
    print("\n\n**BEM VINDO AO JOGO DA FORCA MULTIPLAYER***\n")

    print("----------------------------------------------------------------------------------------------------"
    "\nINSTRUÇÕES: \n"
    "-ESCOLHA QUANTOS JOGADORES QUISER\n"
    "-CHUTE UMA LETRA, SE ERRAR PERDE A VEZ\n"
    "-CADA JOGADOR TEM 7 CHANCES\n"
    "-VOCÊ PODE CHUTAR A PALAVRA TODA A QUALQUER MOMENTO, MAS SE ERRAR, PERDERÁ TODOS OS PONTOS E O JOGO\n"
    "-----------------------------------------------------------------------------------------------------")
    time.sleep(2)

def insere_nome(i):
    return input(f"Insira o nome do jogador {i+1}: ")

def pede_chute():
    chute = input("\nDigite uma letra: ")
    if chute.isdigit()==True:
        print("DIGITE SOMENTE LETRAS")
        chute = pede_chute()
    chute = chute.strip().upper()  
    return chute

def pede_quantidade_de_jogadores():
    num_jogadores = input("Quantos Jogadores? ")
    if num_jogadores.isdigit()==False:
        print("DIGITE SOMENTE NUMEROS")
        num_jogadores =  pede_quantidade_de_jogadores()
    return  int(num_jogadores)

def pergunta_chute(chute):
    os.system("cls")
    print(F"Você digitou a palavra: {chute}")
    print("\n\n -------------------------------ATENÇÃO-------------------------------")
    print("  SE VC CHUTAR A PALAVRA E ERRAR, PERDERÁ O JOGO E TODOS SEUS PONTOS   ")
    print(" ---------------------------------------------------------------------")
    
    decisao = input("Deseja continuar? SIM (S) OU NÃO (N) ").upper()
    while decisao!="S" and decisao!="N": 
        decisao = input("Digite apenas S ou N ").upper()
    if decisao=="S":
        return True
    else:
        return False

def perdeu_jogo():
    os.system("cls")
    print("\n\n\nVOCÊ ERROU A PALAVRA")
    print("GAME OVER PRA VOCÊ\n\n\n")
    time.sleep(2)

def acertou_palavra(pessoa):
    os.system("cls")
    print(f"\n\n\nPARABENS {pessoa['nome']}, VOCÊ ACERTOU A PALAVRA")
    time.sleep(2)

def ninguem_venceu():
    os.system("cls")
    print("\n\nNENHUM DOS JOGADORES VENCEU!")
    print("--------------------------------------------------------")

def apresentacao_vencedores(jogador):
    print(f"{jogador['nome']},você acertou a palavra e fez {jogador['pontos']} pontos")

def define_ranking(lista_de_jogadores):
    ranking = []
    os.system("cls")
    print("RANKING\n")
    for n in range(0,110,10):
        for jogador in lista_de_jogadores:
            if jogador["pontos"]==n:
                ranking.append(jogador)
    p=1
    for jogador in ranking[::-1]:
        print (f" {p} - {jogador['nome']} fez {jogador['pontos']} pontos")
        p+=1
    print("-------------------------------------------------------")

def resultados(lista_de_jogadores):
    vencedores = 0

    for jogador in lista_de_jogadores:
        if jogador["ganhou"]:
            vencedores += 1
    if vencedores == 0:
        ninguem_venceu()
    else:
        
        define_ranking(lista_de_jogadores)