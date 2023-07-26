import forca
import adivinhacao

def escolhaUmJogo():
    print("**************************")
    print("*****Escolha um jogo!*****")
    print("**************************")

    print("(1) Forca  |  (2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar? "))

    if (jogo == 1):
        print("Jogo da forca")
        forca.jogoDaForca()

    elif (jogo == 2):
        print("Jogo da adivinhação")
        adivinhacao.jogoDaAdivinhacao()

if (__name__ == "__main__"):
    escolhaUmJogo()