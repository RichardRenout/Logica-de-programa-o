import os
os.system('cls')

print('Acumulando valores em um variável. ')
soma = 0

for i in range(3):
    soma += int(input('Digite um numero para somar: '))

print(f'\n Valor final da variável soma: {soma}')
