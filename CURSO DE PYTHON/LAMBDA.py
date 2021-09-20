"""
Expresões Lambdas

- Conhecidas por expressões lambdas, são funções sem nomes, ou seja funções anonimas.

# Função em python

def funcao(x):
    return 3 * x + 1

print(funcao(5))


# Expresssão Lambda
lambda x: 3 * x + 1

# como utilizar
calc = lambda x: 3 * x + 1

print(calc(5))
"""

"""
Porque usar Lambda e não criar uma função com def?

# Podemos ter Lambdas com múltiplas entradas
nome_completo = lambda nomes, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' carlota', 'gertrude      '))

- em funções python podemos ter com multiplas entradas ou com nenhuma
_ em Lambda também



# Ex

autores = ['Isaac Asiimov', 'Ray Bradbury', 'Robert Heilen', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)




# Ex 2

# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def quadratica(a, b, c):
    """
    Retorna a função abaixo;
    :return: f(x) = a * x ** 2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c


teste = quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(quadratica(3, 0, 1,)(2))


"""


