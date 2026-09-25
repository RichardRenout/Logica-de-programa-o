import os
os.system('cls')

print('\n Acumulando valores de uma variável.')
soma= 0

print(f'\n Valor inicial de variável soma: {soma}')

for i in range(3):
    numero = int(input('\n Digite um numero para somar: '))
    soma = soma + numero
    print(f'Valor temporário da variável soma: {soma}')

print(f'Valor final da variavel soma: {soma} ')