#  ------ Métodos de listas

lista_01 = ["a", True, 42, "d", 2.56, False, "g"]
print("Lista original: ", lista_01)

# append - Adiciona elemeto ao fim
lista_01.append("Felipe")
print("Depois do append: ", lista_01)

# insert - Adiciona elemeto em uma posição específica
# deslocando os elementos subsequentes
lista_01.insert(2, "Fulano")
print("Depois do insert: ", lista_01)

# extend - Adiciona os elementos de uma lista ao fim de outra
lista_02 = [True, 3, False]
lista_01.extend(lista_02)
print("Depois do extend: ", lista_01)

# pop - remove e retorna o elemento do indice especificado ou 
# o ultimo elemento caso não seja especificado nenhum indice
lista_01.pop()
print("Depois do pop: ", lista_01)
lista_01.pop(4)
print("Depois do pop(4): ", lista_01)

# remove - remove a primeira ocorrencia _do elemento_ especificado
lista_01.remove("Fulano")
print("Depois do remove(Fulano): ", lista_01)

# count - quantidade de vezes que um elemento especifico aparece na lista
print("count(True): ", lista_01.count(True))

# index - indice de determinado elemento na lista
print("index(Felipe): ", lista_01.index("Felipe"))

# sort - ordena uma lista
lista_03 = [4.6, 0.0, 42.0, 3, 99]
print("Antes do sort: ", lista_03)
lista_03.sort()
print("Depois do sort: ", lista_03)
lista_03.sort(reverse=True)
print("Depois do sort(reverse=True): ", lista_03)


#  ------ Funções para listas
# len - tamanho da lista
# sum - soma dos valores da lista
# min - menor valor
# max - maior valor
