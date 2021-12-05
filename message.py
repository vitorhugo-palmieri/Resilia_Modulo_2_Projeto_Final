import time

def intro_jogador(jogador_atual):
    print(f"\nJogando com {jogador_atual['nome']} ")
    time.sleep(2)
    print(f"A palavra tem {len(jogador_atual['palavra_do_jogo'])} letras")

def acertou_letra(chute):
    print("Acertou, tem a letra {} na palavra".format(chute))

def errou_letra():
    print("Voce errou,perdeu a vez!!")

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

def acertou_palavra():
    print("PARABENS VC ACERTOU A PALAVRA")
