"""
Reduce:

A partir do Python versão 3, a função reduce não é mais uma função integrada.
Sendo necessário agora importar para usa-la.
'functools'


Para entender o reduce()

# imagine que tenha uma coleção de dados;

dados = [a1, a2, a3, ..., an]

# E que tenha uma função que receba dois valores

def funcao(x, y):
    return x * y


Assim como no Map e Filter, a função reduce recebe dois parametros: A função e o iterável.
reduce(função, dados)

A Função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # aplica a funçãp nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o res.

    Sendo isso repetido até o final.


Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() irá retornar o resultado final.

"""

# utilizando reduce() para multiplicar os elementos de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 8, 20, 89]

mult = lambda x, y: x * y

res = reduce(mult, dados)

print(res)

# com loop for

res = 1
for n in dados:
    res = res * n

print(res)
