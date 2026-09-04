import os
os.system('cls')

print('\n Solicitando Dados')

login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

login_salvo = 'Richard'
senha_salva = '123@'

if login == login_salvo and senha == senha_salva:
    print('Bem-vindo')
else:
    print("Login ou senha invalido")