import random

def jogoDaAdivinhacao():
    print("*****************")
    print("Bem vindo ao jogo")
    print("Adivinhe o número")
    print("*****************")

    numeroComputador = random.randrange(1, 101)
    tentativasMaximas = 0
    pontos = 1000

    print("Qual desafio você deseja?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = input("Escolha uma dificuldade: ")

    if (nivel == 1):
        tentativasMaximas = 20
    elif (nivel == 2):
        tentativasMaximas = 10
    else:
        tentativasMaximas = 5

    for rodada in range(1, tentativasMaximas + 1):
        print("Tentativa {} de {}".format(rodada, tentativasMaximas))
        chuteUsuario = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chuteUsuario)
        chuteInt = int(chuteUsuario)

        if (chuteInt < 1 or chuteInt > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chuteInt == numeroComputador
        maior = chuteInt > numeroComputador
        menor = chuteInt < numeroComputador

        if (acertou):
            print("Você acertou o número e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O número é maior.")
            elif (menor):
                print("Você errou! o número é menor.")

            pontosPerdidos = abs(numeroComputador - chuteInt)
            pontos = pontos - pontosPerdidos

            if (rodada == tentativasMaximas):
                print("*************************")
                print("Suas tentativas acabaram!")
                print("*************************")
                print("O número secreto era {}. Você fez {} pontos".format(numeroComputador, pontos))

    print("Fim do jogo")