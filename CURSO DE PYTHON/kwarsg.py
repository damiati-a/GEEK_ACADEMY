"""
**KWARDS

Poderiamos chamar este parametro por qualquer nome tambem

- Ele acrescenta valores extras a uma tupla, o kwards exige parametros nomeados, e transforma esses parametros extras
em um dicionário.



def cores(**kwards):
    for pessoa, cor in kwards.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')



cores(a='verde', b='vermelho', c='azul')




# Nas nossas funções podemos ter:
- parametros obrigatórios
- *args
- parametros default
- **kwargs



def funcao(num, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro F')
    else:
        print('Casado top')
    print(kwargs)


funcao(9, 'Jamanta')
funcao(19, 'Claudete', 5, 6, 7, solteiro=True)
funcao(79, 'Pedromina', eu='Não', voce='Ué')
funcao(445, 'Beiçola', 9, 8, 7, solteiro=False)



# desempacotar em **kwargs

def mostra_nomes(*kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Carlão', 'sobrenome': 'Pedrada'}

print(mostra_nomes(**nomes))


# OBS: OS NOMES DAS CHAVES DE UM DICT DEVEM SER OS MESMOS DE UM PARAMETROS DE UMA FUNÇÃO.

"""


