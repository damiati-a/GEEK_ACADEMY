"""
Any & All


all() - Retorna True se todos os elementos do iterável são verdadeiros, ou se está vazio


"""
# EX all()

# False
print(all([0, 1, 2, 3, 4, 5, 6, 7]))
# True
print(all([1, 2, 3, 4, 5, 6, 7]))

# Checagem

nomes = ['Gertrudes', 'Geonisio', 'GigaBAyTE']

print(all([nome[0] == 'G' for nome in nomes]))

# O all verifica se todos estão corretos ou não
# O any verifica se alguns
"""
Para o Any basta ter um elemento verdadeiro para que ele retorne como True
"""
# True
print(any([0, 1, 2, 3, 4]))
# True
nomes = ['Gertrudes', 'Geonisio', 'GigaBAyTE', 'Solene']

print(any([num for num in [4, 5, 6, 7, 8] if num % 2 == 0]))

