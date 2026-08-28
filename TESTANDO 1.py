import os
os.system('cls')

print('\nSolicitando Dados')

primeira_nota = float(input('\nDigite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

print('\nMedia: ',media)

n1 = float(input('\nDigite seu primeiro numero: '))
n2 = float(input('Digite seu segundo numero: '))

soma = (n1+n2)
multiplicacao = (n1*n2)

if n1 > n2:
    print('\nO maior numero é: ',n1)
else:
    print('O maior numero é: ',n2)
if n1 < n2:
    print('O menor numero é: ',n1)
else:
    print('O menor numero é: ',n2)