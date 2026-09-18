import os
os.system('cls')

media = float(input('Digite sua média: '))
faltas = int(input('Digite o numero de faltas: '))

if media >= 7.0 and faltas <= 40:
    print('Aprovado')
else:
    print('Reprovado')