# Calcular preço de venda para produto por quilo.

# Descobrindo o preço do produto pela quantidade de quilos comprados
valor_quilo = float(input("Digite o valor do quilo: "))
quantidade_quilo = float(input("Digite a quantidade de quilos: "))
preco_produto = valor_quilo * quantidade_quilo

print("O preço do produto é de R$", str(preco_produto), "por quilo.")



# Descobrindo o preço do quilo 
preco = float(input("Digite o preço do produto: "))
peso = float(input("Digite o peso do produto em gramas: "))
preco_quilo = (preco * 1000) / peso

print("O preço por quilo do produto é de R$", str(preco_quilo))