"""
Serve para interromper um loop, ou para sair de maneira projetada.
Força uma saída.


"""
# 1
for numero in range(0, 10):
    if numero == 7:
        break
    else:
        print(numero)
print('fim')

# 2
while True:
    comando = input('digite sair para encerrar: ')
    if comando == 'sair':
        break
