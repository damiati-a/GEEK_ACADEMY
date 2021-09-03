numero = float(input('Digite um número: '))
raiz = numero ** 0.5
dobro = numero * 2

if numero >= 0 :
    print(f'O número {numero} é positivo, portanto sua raiz quadrada é {raiz}')
else:
    print(f'O número {numero} é negativo, portando o dobro de seu valor é {dobro}')
