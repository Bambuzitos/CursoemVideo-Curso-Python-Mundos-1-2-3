# Leia seis números inteiros e mostre apenas a soma dos pares.

soma = 0
for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos números pares digitados é {soma}.")