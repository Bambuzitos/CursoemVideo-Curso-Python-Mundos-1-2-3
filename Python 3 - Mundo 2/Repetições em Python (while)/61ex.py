# Mostre os 10 primeiros termos de uma PA usando while.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(termo, end=' ')
    termo += razao
    contador += 1
print("FIM")