import os
os.system('cls')

print('\n Alistamento Obrigatorio')

nome = str(input('\nDigite seu nome: '))
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo (M ou F): ').upper()

if idade >= 18 and sexo == 'M':
    print('\n Alistamento obrigatorio ')
else:
    print('\n Alistamento opcional ')