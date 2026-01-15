# Continue o exercício 61 perguntando se quer mostrar mais termos até digitar 0.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
contador = 1
total_termos = 10
while total_termos != 0:
    while contador <= total_termos:
        print(termo, end=' ')
        termo += razao
        contador += 1
    print()
    total_termos = int(input("Quantos termos você quer mostrar a mais? (0 para sair) "))
print("FIM")