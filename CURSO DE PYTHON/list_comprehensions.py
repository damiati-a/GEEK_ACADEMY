"""
list comprehension
- Utilizando o list comprehension,  nós podemos gerar nosvas listas com dados processados a partir de outro iterável.

# sintaxe

[dado for dado in iteravel]



"""

"""
# exemplos

numeros = [1, 2, 3, 4, 5]
res = []
for numero in numeros:
    res.append(numero * 10)

print(res)"""

"""
Para entender melhor o que acontece devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


"""

"""
res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)
"""
"""
# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2 
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# list comprehension
print([numero * 2 for numero in numeros])
"""
"""
# Ex 1

nome = 'Geek University'
print([letra.upper() for letra in nome])


# Ex 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'cleiton rasta', 'guizao da massa', 'entenda o cassio']
print([caixa_alta(amigo) for amigo in amigos])

# Ex 3
print([numero * 3 for numero in range(1, 10)])

# Ex 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Ex 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""

# PARTE 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares, impares)

# Ex 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)













