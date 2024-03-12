'''
    Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros. Sabe-se que:

    a. O valor de locação de cada carro é 100,00 reais por dia;
    b. O cliente pode locar um único carro por vários dias.

'''

valor_aluguel = 100.00
dias_alugados = int(input("Digite quantos dias o carro ficará alugado: "))
valor_locacao = valor_aluguel * dias_alugados

print("O valor da locação será de R$", str(valor_locacao) + ".")

