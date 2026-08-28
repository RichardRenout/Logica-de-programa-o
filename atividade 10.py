import os
os.system ('cls')

print('\n Solicitando Dados')

n1 = int(input('\nDigite primeiro_numero: '))
n2 = int(input('Digite o segundo_numero: '))

print('\nPrimeiro numero: ',n1)
print('Segundo numero: ',n2)
print('Terceiro numero: ',n3)

if n1 > n2:
    print('\nO numero maior é: ',n1)
else:
    print('O numero maior é: ',n2)
if n1 < n2:
    print('O numero menor é: ',n1)
else:
    print('O numero menor é: ',n2)
