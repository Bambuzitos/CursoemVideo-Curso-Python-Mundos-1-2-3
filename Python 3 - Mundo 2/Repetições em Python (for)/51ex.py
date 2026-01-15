# Leia primeiro termo e razão de uma PA e mostre os 10 primeiros termos.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo_termo = primeiro_termo + (10 - 1) * razao
for termo in range(primeiro_termo, decimo_termo + razao, razao):
    print(termo, end=' ')
print("FIM")