"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Tanto as chaves qaunto os valores podem ser de qualquer tipo de dado.
Eles são separados por :
Podemos misturar os tipos de dados.

print(type({}))


"""
"""
# formas de utilizar um dicionário

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ar': 'Argentina'}

print(paises)
print(type(paises))


paises = dict(br='Brasil', eua='Estados Unidos', ar='Argentina')

print(paises)
print(type(paises))
"""
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ar': 'Argentina'}
# Acessando elementos
# forma 1 - via chave, como em lista/tupla

print(paises['br'])


# forma 2 - via get - forma recomendada

print(paises.get('br'))

# quando o dicionário nao encontrar um valor dentro do get, ele ira retornar como None

print(paises.get('ru'))

- Podemos definir um valor padrão caso não encontremos um valor na chave informada.
"""
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ar': 'Argentina'}

print('br' in paises)  # True
print('ru' in paises)  # chave não existente: False

# - Podemos verificar se uma chave se encontra dentro de um dicionário
"""
"""
- Pode-se usar tuplas e listas como chaves de dicionários.


"""
"""
# adicionar elementos no dicionário

receita = {'janeiro': 100, 'fevereiro': 250, 'março': 320}
print(receita)

# forma 1
receita['abril'] = 400
print(receita)

# forma 2
novo_dado = {'maio': 525}
receita.update(novo_dado)
print(receita)

# Atualização de dados

# forma 1

receita['maio'] = 550
print(receita)

# forma 2

receita.update({'maio': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em dicionários é a mesma.
# Conclusão 2: Em dicionários não podemos ter chaves repetidas.


"""
"""
# Como remover itens de um dict.

receita = {'janeiro': 100, 'fevereiro': 250, 'março': 320}
print(receita)

# Forma 1
retorno = receita.pop('março')

print(retorno)
# neste modo sempre precisa-se passar a chave.
# ao remover um objeto ele sempre retorna o valor removido.

print(receita)

# Forma 2
del receita['fevereiro']
print(receita)

"""
"""
carrinho = []
produto1 = {'nome': 'Garrafão', 'quantidade': 2, 'Preço': 232.00}
produto2 = {'nome': 'Gelol', 'quantidade': 1, 'Preço': 170.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Para se limpar os dados de um dict. Use o modo .clear()
# Para copiar um dict para outro. Use o modo .copy()
# Ou pode-se copiar utilizando o modo de shallow copy.
"""
"""
# Forma não usual de criar dicionários.

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método Fromkeys recebe dois parametros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

"""
