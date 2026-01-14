#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
preco_com_desconto = preco - desconto
print(f"O preço do produto com 5% de desconto é R$ {preco_com_desconto:.2f}.")
