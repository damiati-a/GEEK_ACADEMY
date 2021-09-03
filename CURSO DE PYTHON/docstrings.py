"""
Documentando funções com docstring



"""


def diz_oi():
    """ Uma função que apenas retorna a string 'oi'"""
    return 'Oi'


print(diz_oi.__doc__)


# Podemos ter acesso a documentação de uma função em PY, utilizando a propriedade __doc__
# Podemos ter acesso a documentação também utilizando o help()

def exponencial(num, potencia=2):
    """
    Função que retorna por padrão o quadrado de um número ou número a potencia informada.
    :param num: Número que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial do valor da potencia.
    """
    return num ** potencia


print(exponencial.__doc__)
