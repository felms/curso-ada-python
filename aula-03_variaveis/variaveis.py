# Comentários em Python são feitos assim...

"""
Já comentários de múltiplas linhas
são feitos assim
"""

#  ---- Criando variáveis

# Python tem tipagem dinâmica
nome = "HAL"  # Váriavel str - Strings em Python pode utilizar tanto aspas duplas como aspas simples
idade = "42"  # Variável int

"""
Tipos de variáveis em Python:
- int
- float
- str
- bool (Atenção!! É 'True' e 'False'. Em MAIÚSCULAS)
"""


# Exemplos
idade = 15
altura = 1.90
nome = "Fulano"
eh_destro = False

# Para ver o tipo de uma variável
print(type(idade))
print(type(altura))
print(type(nome))
print(type(eh_destro))

# Obtendo dados da entrada
resposta = input("Que que vc está estudando, véio?\n")
print("Legal!", resposta, "é doido demais!")