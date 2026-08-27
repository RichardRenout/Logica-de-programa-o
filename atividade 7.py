import os
os.system('cls')

n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua nota: '))
n3 = float(input('Digite a sua nota: '))

media = (n1+n2+n3) /(3)

if media >=7:
    resultado  = 'Aprovado'
else: resultado = 'Reprovado'

print(f'media: {media}')
print(f'resultado: {resultado}')