import os
os.system('cls')

nota = int(input('Digite sua nota: '))

if nota >= 0 and nota <= 10:
    print('\n A nota é: ', nota)
else:
    print('A nota deve ser de 0 a 10')