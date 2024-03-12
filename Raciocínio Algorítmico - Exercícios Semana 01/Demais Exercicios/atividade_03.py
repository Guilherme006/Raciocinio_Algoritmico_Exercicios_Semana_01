'''
    Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit. 

    Fórmula: (X ºC x 9/5) + 32
'''

temperatura_celsius = int(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (temperatura_celsius * 9 / 5) + 32

print("A temperatura em Fahrenheit é", str(fahrenheit), "graus.")