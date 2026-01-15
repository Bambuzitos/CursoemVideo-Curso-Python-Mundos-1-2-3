# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salário do comprador: R$"))
anos = int(input("Em quantos anos o comprador vai pagar? "))
prestacao_mensal = valor_casa / (anos * 12)
limite = salario * 0.30
if prestacao_mensal <= limite:
    print(f"Empréstimo aprovado! A prestação mensal será de R${prestacao_mensal:.2f}.")
else:
    print(f"Empréstimo negado! A prestação mensal de R${prestacao_mensal:.2f} excede 30% do salário (R${limite:.2f}).")
