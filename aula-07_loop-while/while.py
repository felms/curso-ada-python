numero_sorteado = 13

numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

while numero_sorteado != numero_escolhido:
    numero_escolhido = int(input("Tente novamente.\nInforme um número entre 1 e 20: "))

print("Você acertou!")