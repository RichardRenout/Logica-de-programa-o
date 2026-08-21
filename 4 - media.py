import os

# Limpa o terminal
os.system('cls')

# '\n= Faz com que pule uma linha abaixo do codigo

print('\n= SOLICITANDO DADOS =')
nome = input('\n= Digite seu nome: ')
idade = int(input('Didigite sua idade: '))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

print('\n= EXIBINDO DADOS =')
print('\n= Nome: ', nome)
print('Idade: ', idade)
print('Primeira nota: ', primeira_nota)
print('Segunda nota: ', segunda_nota)
print('Média: ',media)

