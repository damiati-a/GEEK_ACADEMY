"""
reversed

-> não confunda com a função reverse que inverte as ordens de uma lista.

a reversed é como a função sorted, utilizada para qualquer parametro
ela inverte qualquer iterável

a função reversed retorna um iteravel chamado list_reverseiterator

Pode se converter este valor para qualquer parametro
"""

lista =[1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# lista
print(list(reversed(lista)))
# tupla
print(list(reversed(lista)))
# set
print(set(reversed(lista)))

# Podemos iterar sob um reversed
for letra in reversed('Damiati'):
    print(letra, end='\n')

# loop reverso
for n in reversed(range(0, 10)):
    print(n)
