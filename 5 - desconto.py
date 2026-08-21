import os

#Limpa o terminal
os.system('cls')

print(' \n= SOLICITANDO DADOS =')
valor =float(input('\n= Digite o valor: '))

#CALCULANDO.
#Descontando 10%.

desconto = valor * 0.10
valor_com_desconto = valor - desconto

print(' \n= EXIBINDO DADOS =')
print(' \n= Valor com desconto de 10%: ',valor_com_desconto)

