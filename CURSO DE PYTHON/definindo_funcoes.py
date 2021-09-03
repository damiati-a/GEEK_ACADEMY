"""
DEfinindo funções

- funções são pequenos trechos de códigos que realizam tipos de tarefas específicas.
- Pode ou não receber entradas de dados e pode ou não retornar uma saída de dados.
- Muito uteis para executar procedimentos similares por repetidas vezes.

OBS: Se voce escrever uma função que realiza várias tarefas dentro dela;
é bom sempre fazer uma verificação para que a função seja simplificada.

- Como criar as próprias funções.
-

"""

"""
# Exemplo

cores = ['verde', 'vermelho', 'azul', 'branco']
print(cores)
cores.append('roxo')
print(cores)
"""

"""

- Para definir uma função própria em python:

def nome_da_função(parametros_de_entrada):
    bloco_da_função
    
    
Onde:
nome_da_função: precisa ser sempre escrito com letras minusculas e separados por underline '_'

parametros_de_entrada: são opicionais, onde tendo mais de um, que sejam separados por virgula.

bloco_da_função: tambem chamado de corpo da função, onde o processo da função definida acontece,
podendo ter retorno ou não.


"""
"""

# Definindo uma função


def diz_oi():
    print('oi')




- Veja que dentro de nossas funções podemos utilizar outras funções. Qualquer uma que seja.
- Veja que nossa função executa apenas uma tarefa, no caso printar 'oi'.
- Veja que esta função não recebe nenhum parametro de entrada e não possui nenhum retorno.



# Utilizando uma função

# Chamando uma função

diz_oi()
"""
"""
Nunca esqueça de utilizar os parenteses ao executar uma função, ou a mesma ira lhe retornar um erro.
"""


# Exemplo 2

def cantar_parabens():
    print('Parabéns para você \nNesta data querida \nMuitas felicidades \nMuitos anos de vida.')
    print('RÁ-TIM-BUM\nPARABÉNS!!!')


for n in range(5):
    cantar_parabens()


"""
Podemos criar uma função atraves de outra função e executar a nova função atraves de uma variavel.
"""

canta = cantar_parabens
canta()

