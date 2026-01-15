# Leia o peso de cinco pessoas e mostre o maior e o menor valor.

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (kg): "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso digitado foi {maior} kg.")
print(f"O menor peso digitado foi {menor} kg.")