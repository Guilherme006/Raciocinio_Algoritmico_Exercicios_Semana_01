# Calcular sua idade em meses.

ano_atual = 2024
ano_nascimento = int(input("Digite o ano que você nasceu: "))
idade_em_anos = 2024 - ano_nascimento
meses = idade_em_anos * 12
mes_nascimento = int(input("Digite o número do seu mês de nascimento: "))
mes_atual = int(input("Digite o número do mês atual: "))

idade_em_meses = (meses - mes_nascimento) + mes_atual

print("Sua idade em meses é", str(idade_em_meses))