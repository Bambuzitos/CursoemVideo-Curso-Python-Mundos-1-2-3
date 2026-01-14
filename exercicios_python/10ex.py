# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite o valor em R$ que você tem na carteira: R$ ")) 
dolar_antigo = real / 3.27
print(f"Com R$ {real:.2f} você podia comprar US$ {dolar_antigo:.2f}.")
dolar_atual = real / 5.10
print(f"Com R$ {real:.2f} você pode comprar US$ {dolar_atual:.2f}.")
euro = real / 5.50
print(f"Com R$ {real:.2f} você pode comprar € {euro:.2f}.")
iene = real / 0.036
print(f"Com R$ {real:.2f} você pode comprar ¥ {iene:.2f}.")

