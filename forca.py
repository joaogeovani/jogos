import random


def jogoDaForca():

    mensagemDeAbertura()
    palavraSecreta = buscarPalavras()
    letrasCertas = imprimeLetras(palavraSecreta)
    print(letrasCertas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        escolhaLetra = chuteUsuario()

        if(escolhaLetra in palavraSecreta):
            acertouLetra(escolhaLetra, letrasCertas, palavraSecreta)

        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasCertas
        print(letrasCertas)

    if(acertou):
        mensagemVencedor()
    else:
        mensagemPerdedor(palavraSecreta)

    print("Fim do jogo")


def mensagemDeAbertura():
    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

def buscarPalavras():
    arquivo = open("palavrasSecretas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def imprimeLetras(palavra):
    return ["_" for letra in palavra]

def chuteUsuario():
    escolhaLetra = input("Qual letra? ")
    escolhaLetra = escolhaLetra.strip().upper()
    return escolhaLetra

def acertouLetra(escolhaLetra, letrasCertas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (escolhaLetra.upper() == letra.upper()):
            letrasCertas[index] = letra
        index += 1

def mensagemVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagemPerdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogoDaForca()