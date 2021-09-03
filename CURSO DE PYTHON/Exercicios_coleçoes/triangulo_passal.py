# triangulo de pascal


while True:
    numeros = int(input('Digite a quantidade de linhas para acrescentar ao Triângulo de Pascal: '))
    if numeros > 0:
        break
prox_linha = ['1']
for linha in range(1, numeros + 1):
    print((numeros - len(prox_linha)) * ' ', ' '.join(prox_linha))
    for indice in range(len(prox_linha)):
        prox_linha[indice] = int(prox_linha[indice])
    prox_linha.append(0)
    prox_linha.insert(0, 0)
    for indice in range(len(prox_linha) - 1):
        prox_linha[indice] = str(prox_linha[indice] + prox_linha[indice + 1])
    prox_linha.pop()

