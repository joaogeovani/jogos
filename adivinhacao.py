print("*****************")
print("Bem vindo ao jogo")
print("Adivinhe o número")
print("*****************")

numeroComputador = 47
tentativasMaximas = 3

for rodada in range(1, tentativasMaximas +1):
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
        print("Você acertou o número!")
        break
    else:
        if (maior):
            print("Você errou! O número é maior.")
        elif (menor):
            print("Você errou! o número é menor.")

print("Fim do jogo")