print("*****************")
print("Bem vindo ao jogo")
print("Adivinhe o número")
print("*****************")

numeroComputador = 47

chuteUsuario = input("Digite o seu número: ")
print("Você digitou: ", chuteUsuario)
chuteInt = int(chuteUsuario)

acertou = chuteInt == numeroComputador
maior = chuteInt > numeroComputador
menor = chuteInt < numeroComputador

if (acertou):
    print("Você acertou o número!")
else:
    if(maior):
        print("Você errou! O número é maior.")
    elif(menor):
        print("Você errou! o número é menor.")

print("Fim do jogo")