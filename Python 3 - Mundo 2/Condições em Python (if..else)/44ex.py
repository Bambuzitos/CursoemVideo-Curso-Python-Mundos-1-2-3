# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

preco_normal = float(input("Digite o preço do produto: R$"))
print("Escolha a condição de pagamento:")
print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço formal)")
print("4 - 3x ou mais no cartão (20% de juros)")
opcao = int(input("Sua opção: "))

if opcao == 1:
    preco_final = preco_normal * 0.90
    print(f"Preço final com 10% de desconto: R${preco_final:.2f}.")
elif opcao == 2:
    preco_final = preco_normal * 0.95
    print(f"Preço final com 5% de desconto: R${preco_final:.2f}.")
elif opcao == 3:
    preco_final = preco_normal
    print(f"Preço final sem desconto: R${preco_final:.2f}.")
elif opcao == 4:
    preco_final = preco_normal * 1.20
    print(f"Preço final com 20% de juros: R${preco_final:.2f}.")
else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    