#  ------ Funções

# Definindo funções
# Em python funções são definidas
# utilizando a palavra reservada 'def'

def primeira_funcao(nome, idade):
    status = "maior de idade" if idade >= 18 else "menor de idade"
    print(f"Olá {nome}! Você é {status}")

primeira_funcao("Fulano", 42)
primeira_funcao("Ciclano", 17)

# Funções com parametros default
def segunda_funcao(nome, idade=25):
    print(f"Olá {nome}! Você é tem {idade} anos de idade")

segunda_funcao("Fulano")
segunda_funcao("Ciclano", 17)
