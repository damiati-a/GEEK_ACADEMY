"""
Funções com retorno


Quando uma função não retorna nenhum valor, o retorno é None.

Funções com retorno devem utilizar a palavra 'return'


def quadrado7():
    return 7 * 7


print(quadrado7())


def oi():
    return 'Oi'


print(oi())




# Pode-se ter varios retornos numa função

def funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(funcao())

# Funções podem ser importadas no terminal também



# função cara ou coroa

from random import random


def moeda():  # Gera um valor pseudo randomico, entre 0 e 1.
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(moeda())

"""
