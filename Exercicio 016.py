import os
os.system('cls')

n1 = float(input('Digite seu primeiro numero: '))
n2 = float(input('Digite seu segundo numero: '))
n3 = float(input('Digite seu terceiro numero: '))

if n1 + n2 < n3:
    print('A + B É MENOR QUE C')
else:
    print('A + B É MAIOR QUE C')
