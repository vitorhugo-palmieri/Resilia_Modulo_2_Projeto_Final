import time

def intro_jogador(jogador_atual):
    print(f"\n\nJogando com {jogador_atual['nome']} ")
    time.sleep(2)
    print(f"\nA palavra tem {len(jogador_atual['palavra_do_jogo'])} letras")

def acertou_letra(chute):
    print("Acertou, tem a letra {} na palavra".format(chute))

def errou_letra(jogador,chute):
    print("Voce errou!!")
    jogador['letras_erradas'].append(chute)

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

def pergunta_chute():
    print("SE VC CHUTAR A PALAVRA E ERRAR PERDERÁ O JOGO")
    decisao = input("Deseja continuar? S/N ").upper()
    while decisao!="S" and decisao!="N": 
        decisao = input("Digite apenas S ou N ").upper()
    if decisao=="S":
        return True
    else:
        return False

def perdeu_jogo():
    print("------------------VOCÊ ERROU------------------")
    print("------------------GAME OVER------------------")

def acertou_palavra(pessoa):
    print(f"\nPARABENS {pessoa['nome']}, você acertou a palavra!")

def ninguem_venceu():
    print("\n\nNENHUM DOS JOGADORES VENCEU!")

def apresentacao_vencedores(jogador):
    print(f"{jogador['nome']},voce venceu!!")