import os
os.system('cls')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)

if imc <= 18.5:
    resultado = 'Abaixo do peso.'
elif imc <= 24.9:
    resultado = 'Peso ideal (parabéns).'
elif imc <=
