# Leia nome e preço de vários produtos. Ao final, mostre:
# total gasto  
# quantos produtos custam mais de R$1000  
# nome do produto mais barato  

total_gasto = 0
quantidade_produtos_mais_1000 = 0
produto_mais_barato = ""
preco_produto_mais_barato = 0
while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))
    total_gasto += preco_produto
    if preco_produto > 1000:
        quantidade_produtos_mais_1000 += 1
    if produto_mais_barato == "" or preco_produto < preco_produto_mais_barato:
        produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break
print(f"O total gasto na compra foi R${total_gasto:.2f}.")
print(f"Temos {quantidade_produtos_mais_1000} produtos que custam mais de R$1000.")
print(f"O produto mais barato foi {produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}.")
