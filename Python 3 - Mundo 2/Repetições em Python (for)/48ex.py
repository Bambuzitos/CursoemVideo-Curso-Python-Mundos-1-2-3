# Calcule a soma dos múltiplos de 3 entre 1 e 500.

soma = 0
for numero in range(1, 501):
    if numero % 3 == 0:
        soma += numero
print(f"A soma dos múltiplos de 3 entre 1 e 500 é {soma}.")
