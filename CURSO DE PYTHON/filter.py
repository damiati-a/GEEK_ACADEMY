"""

Filter:

filter() - serve para filtrar dados de uma determinada coleção

valores = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

media = (sum(valores)) / len(valores)

print(media)



import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média utilizando o mean()
media = statistics.mean(dados)
print(f'média = {media}')

# OBS: Assim como o Map, a filter recebe apenas dois parametros, 1 função e 1 iterável.

res = filter(lambda x: x < media, dados)
print(list(res))

print(f'Novamente: {list(res)}')
# Assim como na Map, após utilizar os dados de filter, os dados são excluídos da memória.



# Usar o filter para remover dados faltantes
paises = ['', 'Argentina', '', 'Brasil', '', '', 'Equador', 'Colombia']
print(paises)

res = filter(None, paises)

print(list(res))

# Com Lambda para remover dados faltantes
paises = ['', 'Argentina', '', 'Brasil', '', '', 'Equador', 'Colombia']
print(paises)

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

"""
"""
# A DIFERENÇA ENTRE MAP() E FILTER() É:
# MAP() -> RECEBE DOIS PARAMETROS, UMA FUNÇÃO E UM ITERÁVEL E RETORNA UM OBJETO MAPEANDO A FUNÇÃO PARA CADA ELEMENTO DO ITERÁVEL.
# FILTER() -> RECEBE DOIS PARAMETROS, UMA FUNÇÃO E UM ITERÁVEL E RETORNA UM OBJETO FILTRANDO APENAS OS ELEMENTROS DE ACORDO COM A FUNÇÃO.
"""
# EX MAIS COMPLEXO

# Forma 1

usuarios = [
    {"usarname": "samuelinton123", "tweets": ["eu adoro bolos", "eu adoro pizza"]},
    {"usarname": "jeff_bala", "tweets": ["eu quero café"]},
    {"usarname": "gaugau", "tweets": ["eu vou te dar ban", "jaca no palito"]},
    {"usarname": "f_total", "tweets": []},
    {"usarname": "gegelson", "tweets": []}
]
print(usuarios)

# Filtrar os usuários que estão inativos no twitter

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# forma 2
usuarios = [
    {"usarname": "samuelinton123", "tweets": ["eu adoro bolos", "eu adoro pizza"]},
    {"usarname": "jeff_bala", "tweets": ["eu quero café"]},
    {"usarname": "gaugau", "tweets": ["eu vou te dar ban", "jaca no palito"]},
    {"usarname": "f_total", "tweets": []},
    {"usarname": "gegelson", "tweets": []}
]
print(usuarios)

# Filtrar os usuários que estão inativos no twitter

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar Map() e filter()

nomes = ['Vanessa', 'Maria', 'Ana']
# devemos criar uma lista contendo 'Sua instrutora é a?' + nome, desde que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é a Dona {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
