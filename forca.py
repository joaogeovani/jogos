
def jogoDaForca():
    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

    palavraSecreta = "gato"

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        escolhaLetra = input("Qual letra? ")
        escolhaLetra = escolhaLetra.strip()

        index = 0
        for letra in palavraSecreta:
            if (escolhaLetra.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogoDaForca()