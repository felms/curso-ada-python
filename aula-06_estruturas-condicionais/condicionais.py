# Estruturas Condicionais

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


media = float(input("Informe a média do estudante: "))

if media >= 7.0:
    print("Aprovado!")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado.")
