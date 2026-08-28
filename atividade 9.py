import os
os.system('cls')

idade = int(input('Digite sua idade: '))

if idade >=18:
    print('Você é obrigado a votar')
elif idade >= 65:
    print('Você vota opcionalmente')
elif idade == 17:
    print('Você vota opcionalmente')
elif idade == 16:
    print('Você vota opcionalmente')
elif idade <= 15:
    print('Você não pode votar')
