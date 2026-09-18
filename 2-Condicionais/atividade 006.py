import os
os.system('cls')

print('\nSolicitando Dados')

n1 = float(input('\nDigite seu numero: '))
n2 = float(input('Digite seu numero: '))

media = (n1+n2) / 2
soma = (n1+n2)
produto = (n1*n2)

print('Media: ', media)
print('Soma: ',soma)
print('Produto: ', produto)

if n1 > n2:
    print('É maior',n1)
else:
    print('É maior',n2)
if n2 > n1:
    print('É menor',n1)
else:
    print('É menor',n2)