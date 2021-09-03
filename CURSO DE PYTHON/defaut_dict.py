"""
Defaut Dict

# recap dicionarios
 Ele não apresenta o KeyError

Ao criar um dicionario utilizando o defaut dict, se informa um valor = defaut,
podendo utilizar a lambda para isso. Este valor será utilizado sempre que não houver um definido.

OBS: Lambda são funções sem nomes, que podem ou não receber parametros de entrada.

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programação python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)

"""

