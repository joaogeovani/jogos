print("*****************")
print("Bem vindo ao jogo")
print("Adivinhe o número")
print("*****************")

numeroComputador = 47

chuteUsuario = input("Digite o seu número: ")
print("Você digitou: ", chuteUsuario)
chuteInt = int(chuteUsuario)

if (numeroComputador == chuteInt):
    print("Você acertou o número!")
else:
    print("Você errou o número!")

print("Fim do jogo")