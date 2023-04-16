#  ------ Dicionarios

# Dicionarios são a implementação de Python
# dos Associative Arrays ou Maps

# --- Dicionario
dict_01 = {"nome": "Fulano", "idade": 42, "altura": 1.74}
print("dict_01:", dict_01)
print("dict_01[\"nome\"]:", dict_01["nome"])

# --- Dicionario Vazio
dict_02 = {}
dict_03 = dict()

# --- Adicionando elementos ao dicionario
dict_01["profissão"] = "vagabundo"
print("Adicionando chaves - dict_01: ", dict_01)

# --- Update
dict_01["altura"] = 1.77
print("Depois do Update - dict_01: ", dict_01)

# --- Iteração
print("\nIteração:")
for chave in dict_01:
    print(f"Chave: {chave} -> Valor: {dict_01[chave]}")

# --- Testando a existencia de uma chave
print("A chave \'peso\' existe no dicionário?", "peso" in dict_01)
print("A chave \'altura\' existe no dicionário?", "altura" in dict_01)