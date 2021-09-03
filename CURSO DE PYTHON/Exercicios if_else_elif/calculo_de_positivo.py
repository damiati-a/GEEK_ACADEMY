num = float(input('Digite um número: '))
dobro = num * 2
raiz = num ** 0.5

if num >= 0:
    print(f'O dobro de {num} é {dobro} e sua raíz é {raiz}')
else:
    print(f'{num} é negativo, e apenas numeros positivos são aceitos')

