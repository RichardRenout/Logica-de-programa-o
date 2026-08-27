import os
os.system('cls')

print('\n SOLICITANDO DADOS')

#---------------------------------------------------
#Criando as variaveis:

nome = str
idade = int
altura = float
peso = float

#---------------------------------------------------
#Aplicando valores:

nome: 'Marta'
idade: 28
altura: 1.85
peso: 65.500

#---------------------------------------------------
#Aplicando codigos:

nome = input('\nDigite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

#---------------------------------------------------
#Aplicando o codigo separadamente:

numero = int(input('\nDigite seu numero: '))

#Calculando:

antecessor = numero -1
sucessor = numero +1

print('\nExibindo Dados')
print('\nAntecessor: ',antecessor)
print('Sucessor: ', sucessor)

#--------------------------------------------------