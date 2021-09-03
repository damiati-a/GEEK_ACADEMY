"""
Módulo collections - Counter

Collections -> high performance container Datetypes
Recebe o iterável como um paramentro e cria um objeto do tipo collections counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada com0o um paramentro
e como um valor e quantidade de ocorrencias desse elemento.

from collections import Counter
lista = [1, 1, 1, 1, 1, 1, 2, 3, 7]
# ele verifica quantas ocorrencias tem do mesmo valor
# no caso de textos, a contagem é por palavras
res = Counter(lista)

print(type(res))

print(res)

"""
