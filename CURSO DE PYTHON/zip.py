"""
Zip

zip() -> crria um iterável(zip object) que agrega elemento de cada um dos iteraveis passado como entrada em pares.

Ele forma tuplas juntando pares dos valores passados.
Ele se baseia no tamanho da menor lista para formar os pares.



# EX
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# pode se gerar lista, tuplas e conjuntos
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

"""
# Ex 2
prova1 = [80, 97, 45]
prova2 = [95, 69, 77]
alunos = ['Martinho', 'Rita', 'Elielsion']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)