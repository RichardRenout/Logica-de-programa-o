import os

#LIMPA O TERMINAL
os.system("cls")

# SOLICITANDO DADOS.
# INPUT ADICIONA O QUE FOR DIGITADO NO TERMINAL NA VARIAVEL COMO TEXTO

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#INT() CONVERTE O QUE FOI DIGITADO EM INTEIRO (NUMEROS INTEIROS)
idade = int(input('Digite sua idade: '))

#FLOAT() CONVERTE O QUE FOI DIGITADO EM FLOAT (NUMEROS REAIS)
peso = float(input('Digite seu peso: '))
altura =float(input('Digite sua altura: '))

#MOSTRANDO DADOS.
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ',idade)
print('Peso: ', peso)
print('Altura: ', altura)
