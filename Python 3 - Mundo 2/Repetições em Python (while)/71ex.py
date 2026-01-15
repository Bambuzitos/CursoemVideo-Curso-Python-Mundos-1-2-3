# Simule um caixa eletrônico informando quantas cédulas de cada valor serão entregues conforme o saque.

print("=== Caixa Eletrônico ===")
valor_saque = int(input("Digite o valor que deseja sacar: R$"))
cedulas = [200, 100, 50, 20, 10, 5, 2, 1]  
quantidade_cedulas = {}

for cedula in cedulas:
    if valor_saque >= cedula:
        quantidade = valor_saque // cedula
        valor_saque -= quantidade * cedula
        quantidade_cedulas[cedula] = quantidade
for cedula, quantidade in quantidade_cedulas.items():
    print(f"Cédulas de R${cedula}: {quantidade}")
print("Obrigado por usar o caixa eletrônico!")
