import os
os.system('cls')

maca = int(input('Digite a quantidade desejada: '))

#criando n1 e n2 com o objetivo de criar 2 tipos de possiveis resultado, depois de aplicar a logica

n1 = maca * 1.30
n2 = maca * 1.00


if n1 >= 12:
    print('As maçãs são 1,00 cada')
    print('Com desconto')

elif n2 <= 11:
    print('As maçãs são 1,30 cada')
    print('Sem desconto')


