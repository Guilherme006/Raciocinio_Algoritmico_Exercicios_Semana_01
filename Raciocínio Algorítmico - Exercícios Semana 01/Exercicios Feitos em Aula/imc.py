'''
    Crie um algoritmo que calcula o IMC e imprime o resultado

    Fórmula - IMC = peso / altura²
'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

print("Seu IMC é:", str(imc))

