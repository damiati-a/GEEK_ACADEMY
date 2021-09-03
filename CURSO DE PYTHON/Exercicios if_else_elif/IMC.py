altura = float(input('Informe sua altura para cálculo do IMC: '))
peso = float(input('Informe seu peso para cálculo do IMC: '))


imc = peso / altura ** 2

print(f'Seu IMC é {imc}')

if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5:
    print('Você está saudável!')
elif imc >= 25.0:
    print('Você está com excesso de peso!')
elif imc >= 30.0:
    print('Você está com Obesidade de grau 1!')
elif imc >= 35.0:
    print('Você está com obesidade de rau 2!')
elif imc >= 40.0:
    print('Você está com obesidade mórbida!')

