import os
os.system('cls')

print('Solicitando Dados')

QUANTIDADE_NOTA = 4
soma_nota = 0.0

for i in range(QUANTIDADE_NOTA):
    soma_nota += float(input('Digite uma nota: '))

media = soma_nota / QUANTIDADE_NOTA


print(f'Media: {media}') 