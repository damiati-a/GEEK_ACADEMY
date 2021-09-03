"""
*args -> O args é um parametro de entrada de uma função, significa que voce podera o chamar de qualquer coisa
desde que considere o *


O que é o args?
- O parametro de args usado em uma função colocam os valores extras informados como entrada em uma tupla.
Então desde ja lembre-se que tuplas são imutáveis.



# Entendendo o args


def soma_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# ou apenas colocando o return sum(args)


print(soma_todos())
print(soma_todos(2))
print(soma_todos(5, 7, 90))
print(soma_todos(10, -1, 55, 7))



def verifica(*args):
    if 'Geek' in args and 'university' in args:
        return 'Bem vindo Geek'
    return 'Eu não tenho certeza de quem você é...'


print(verifica())
print(verifica(1, True, 'University', 'Geek'))



def soma_todos(*args):
    return sum(args)


# desempacotando listas usando o *args
numeros = [1, 3, 4, 5, 6, 7, 9]
print(soma_todos(*numeros))

# o * serve para informar ao Python que estamos passando como argumento uma coleção de dados,
# desta forma ele sabe que precisará desempacotar estes dados para os utilizar após.

"""
