"""
Conjuntos

- COnjuntos em qualquer linguagem de programação, assim como na matemática.


- Em python conjuntos são chamados de sets()

- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via índice, conjuntos não são indexados.


Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordem deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com {}
- Um dict tem chave/valor.
- um sets tem apenas valor.
"""
"""
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)
print(type(s))
# Ele nao imprime os valores repetidos e não gera erros.
# Sets não gera ordenação

"""
"""
# Assim como todo outro conjunto python, podemos colocar tipos de dados misturados em sets.
# Sets podem ser iterados normalmente


cidades = ['MG', 'SP', 'PR', 'RR', 'MS', 'SP', 'MG']

print(cidades)
print(len(set(cidades)))
"""

"""
# adicionar elementos num conjunto
s = {1, 2, 4}
s.add(5)
s.add(4)  # duplicidade é apenas ignorado, não gera erros
print(s)
"""
"""
# remover elementos de um conjunto
s = {1, 2, 4}
s.remove(2)
print(s)

s.discard(1)
print(s)

# copiando um valor pra um conjunto
s = {1, 2, 4}
print(s)

# forma 1 - deep copy
novo = s.copy()
print(novo)

novo.add(5)
print(novo)

# forma 2 - shallow copy

s = {1, 2, 4}
print(s)
novo = s
novo.add(7)
print(novo)
print(s)

# utilizando o .clear() se remove todos os elementos do conjunto
"""
"""
# metodos matemáticos de um conjunto

# conjunto 1 - estudante python
# conjunto 2 - estudante java

estudantes_py = {'Marcos', 'Daniel', 'André', 'Xeroline', 'Fedora'}
estudantes_ja = {'Gertrudes', 'André', 'Félix', 'Xeroline'}

# alguns alunos estudam as duas linguagens
# precisamos gerar um conjunto com nomes de estudantes de formas únicas

# forma 1 - UNION
unicos1 = estudantes_py.union(estudantes_ja)
print(unicos1)

# forma 2 - pipe |
unicos2 = estudantes_py | estudantes_ja
print(unicos2)

"""
"""
# conjunto de estudantes que estão em ambos os cursos
estudantes_py = {'Marcos', 'Daniel', 'André', 'Xeroline', 'Fedora'}
estudantes_ja = {'Gertrudes', 'André', 'Félix', 'Xeroline'}

# forma 1 - intersection
ambos1 = estudantes_py.intersection(estudantes_ja)
print(ambos1)

# forma 2 - &
ambos2 = estudantes_py & estudantes_ja
print(ambos2)

# estudantes de um só curso

estudantes_py = {'Marcos', 'Daniel', 'André', 'Xeroline', 'Fedora'}
estudantes_ja = {'Gertrudes', 'André', 'Félix', 'Xeroline'}

# utiliza o difference
so_py = estudantes_py.difference(estudantes_ja)
print(so_py)
so_ja = estudantes_ja.difference(estudantes_py)
print(so_ja)


s = {1, 2, 3, 5, 6, 7, 8}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""
