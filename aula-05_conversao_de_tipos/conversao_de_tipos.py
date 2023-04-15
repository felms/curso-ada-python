# Conversão de tipos

idade = '15'
print(idade, type(idade))

numero_01 = '01'
numero_02 = '02'

# converter para int
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# converter para str
idade_str = str(idade)

print(idade_str, type(idade_str))

# o mesmo é valido para float -> float(_something)
# o mesmo é valido para bool -> bool(_something)

# Obs: a função 'input' vai retornar o valor de entrada como uma string