import os
os.system('cls')

print('\n Solicitando Dados')

pares = 0
impares = 0

for i in range(5):
    numeros = int(input('Digite seu numero: '))
    if numeros % 2 == 0:
        pares = pares +1
    else:
        impares = impares +1

print(f'Quantidade de pares são: {pares}')
print(f'Quantidade de impares são: {impares}')
