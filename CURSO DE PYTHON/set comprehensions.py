"""
Set = { }
- Não aceita valores repetidos;
- Não mantém a ordenação;
- Diferente de listas e dicionários

"""

# Ex 1

numeros = {num for num in range(1, 7)}
print(numeros)

# Ex 2
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Alterando a estrutura para um dict

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Ex 3

letras = {letra for letra in 'Geek University'}

print(letras)
