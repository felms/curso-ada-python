# --- Lista
lista_01 = [2.5, 4.9, 42.0]

# --- Lista vazia
lista_02 = []
lista_02_1 = list() # Cria uma lista vazia

# --- Listas podem ter valores de diferentes tipos
lista_03 = ["a", True, 4, 7.906]

# --- Inclusive listas podem armazenar outras listas
lista_04 = [7, "Fulano", [True, "Ciclano", 42]] 

# --- Indexação
idade = lista_04[0]
print(lista_04[2][1]) # Imprime "Ciclano"
print(lista_04[-2]) # Imprime "Fulano"

# --- Slices
lista_05 = [2.5, 4.9, "Ciclano", 42.0, "a", True, 4, 7.906]
print(lista_05[0:3]) # Imprime os itens dos indices de 0 a 3 (exclusive): 
                     # '2.5', '4.9' e "Ciclano"
print(lista_05[3:])  # Imprime os itens do indice 3 até o fim da lista
print(lista_05[1:6:2])  # Imprime os itens dos indices de 1 a 6 com step 2


# --- Iterando uma lista
print("\n--- Lista 05 utilizando os elementos")
for item in lista_05:
    print(item)


print("\n--- Lista 05 utilizando os indices")
for i in range(len(lista_05)):
    print(lista_05[i])