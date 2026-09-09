import os
os.system('cls')

dia = input('Digite o dia da semana: ')

match dia:
    case "segunda":
        print("Hoje é segunda-feira.")
    case "terça":
        print("Hoje é terça-feira.")
    case "quarta":
        print("Hoje é quarta-feira.")
    case "quinta":
        print("Hpje é quinta-feira.")
    case "sexta":
        print("Hoje é sexta-feira.")
    case "sabado" |"domingo":
        print("Hojé é fim de semana")
    case _:
        print("Dia invalidao")

print(dia)

print("===  FIM ===")