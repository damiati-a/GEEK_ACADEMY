soma = maior = menor = 0
quantidade = 0

for numero in range(1, 11):
    valor = int(input(f'Digite o {numero} valor: '))
    soma += valor
    quantidade += 1

    if quantidade == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'O menor valor lido foi {menor} e o maior valor foi {maior}')
