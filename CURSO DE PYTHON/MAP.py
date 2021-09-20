"""
MAP:



Com Map, fazemos o mapeamento de valores para a função.


import math


def area(r):
    """
'''
     Calcula a área de um círculo com raio r
   '''

"""    return math.pi * (r ** 2)
"""

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for r in raios:
    areas.append((area(r)))

print(area)

# Forma 2 - Com Map

# Map é uma função que recebe dois parametros, o primeiro a função, o segundo um iterável

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))


# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# O retorno de Map, só retorna uma vez e depois ele limpa a memória, ao tentar executar novamente, ele retorna o vazio.


# Ex 2

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 27), ('Tókio', 23), ('São Paulo', 17)]
print(cidades)
# Formula do Farnhereit
# f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

# A função passada para o Map, recebe apenas 1 parametro.

