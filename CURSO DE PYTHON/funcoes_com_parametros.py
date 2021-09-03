"""
FUNÇÕES COM PARÂMETRO

- Funções que recebem dados para serem processados dentro da mesma.

Em um programa qualquer geralmente se tem :
entranda -> processamento -> saída

Temos funções que:
- Não possuem entradas;
- Não possuem saídas;
- Possuem entradas mas não possuem saídas;
- Possuem saídas e não possuem entradas;
- Possuem tanto entrada quanto saída.




def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(5))
print(quadrado(2))


# Se a função tem uma saída, é obrigatório informar um valor de parametro.



# Funções podem ter n parametros de entrada, recebendo quantos valores forem necessários, separados sempre por ','.

def outra(num1, num2, msg):
    return (num1 + num2) * msg


print(outra(1, 8, 'jajaja'))


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Sidiney', 'Joansson CJ'))

# A ordem dos parametros importa

# Caso utilizemos nomes para os parametros, assim poderiamos utiliza-los em qualquer ordem.

print(nome_completo(nome='salve', sobrenome='cachorros'))

# sempre colocar nomes claros nos parametros

"""

"""
FUNÇÕES COM PARAMETRO PADRÃO
(Default)

# EX DE FUNÇÃO ONDE A PASSAGEM DE PARAMETROS É OPICIONAL
print('Geek University')
print()

EX DE FUNÇÃO ONDE A PASSAGEM DE PARAMETROS É OBRIGATÓRIA
print(quadradro(3))
print(quadrado())


def exponencial(numero, potencia=2):  # definindo como padrão o valor da potencia
    return numero ** potencia


print(exponencial(3))  # Por padrão a função eleva aoa quadrado
print(exponencial(2, 5))  # Elevada a potencia informada pelo usuario

# Em funções python, os parametros defaut devem sempre estar ao final da declaração.

# ERRO
def teste(numero=2, potencia):
    return numero ** potencia

print(teste(2))



# Porque utilizar parametros com funções default?
- Nos permite ter mais flexibilidade nas funções;
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de códigos;

# Tipos de dados que pode-se usar o default
- Numeros, strings, floats, bool, inteiros, listas, tuplas, dict, funções e etc


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, sub))




- Váriavel global sempre informada fora das funções definidas;
- Se tivermos uma variavel local com o mesmo nome que uma variavel global, a local se sobresai.

# Variaveis globais, se puder. Evite.


# Utilizando uma variavel global dentro de uma local

# forma errada
total = 0


def incrementa():
    total = total + 1
    return total


print(incrementa())


# forma correta

total = 0


def incrementa():
    global total  # Solicitando o uso da variavel global(descrita fora da função)
    total = total + 1
    return total


print(incrementa())



# Como declarar funções dentro de uma função

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())
print(fora())

print(dentro())   #Erro

"""


