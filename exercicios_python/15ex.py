# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
preco_por_dia = 60
preco_por_km = 0.15
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)
print(f"O custo total do aluguel do carro é R$ {custo_total:.2f}.")