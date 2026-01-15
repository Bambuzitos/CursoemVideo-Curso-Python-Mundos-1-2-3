# Mostre tabuadas até o usuário digitar um número negativo (encerra o programa).

while True:
    num = int(input("Digite um número para ver sua tabuada (negativo para sair): "))
    if num < 0:
        print("Programa encerrado.")
        break
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i:2} = {resultado}")
    print("-" * 20)
