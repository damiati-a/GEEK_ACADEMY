# ler uma matrix 4x4 e escrever qual a linha e a coluna maior


for linha in range(0, 4):
    for coluna in range(0, 4):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]'))
for linha in range(0, 4):
    for coluna in range(0, 4):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()

maior_linha = 0
maior_coluna = 0
maior = matriz[0][0]
for linha in range(0, 4):
    if maior < matriz[linha][coluna]:
        maior = matriz[linha][coluna]
        maior_linha = linha
        maior_coluna = coluna
print(f'linha maior = {linha}, coluna maior = {coluna}')
