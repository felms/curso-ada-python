# Loop For

for i in range(10): # Range de 0 até n - 1
    print(f"Index: {i}") # interpolação de strings: coloco a letra 'f' antes
                         # da string e coloco o valor utilizado entre chaves

print("\n-----\n")

for i in range(2, 13): # Range não inclusivo i.e.:  Vai de 2 a 12
    print(f"Index in range: {i}")

print("\n-----\n")

for i in range(2, 45, 6): # range(start, end, step)
    print(f"Index in range: {i}")
