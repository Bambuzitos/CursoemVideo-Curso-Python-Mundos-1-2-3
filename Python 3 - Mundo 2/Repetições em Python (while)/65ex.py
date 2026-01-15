# Leia vários números e ao final mostre:
# - média  
# - maior valor  
# - menor valor  
# Sempre perguntando se quer continuar.

contador = 0
soma = 0
maior = float('-inf')
menor = float('inf')
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
if contador > 0:
    media = soma / contador
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("Nenhum número foi digitado.")