# Leia um número inteiro e diga se é primo.

numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"O número {numero} não é primo.")
            break
    else:
        print(f"O número {numero} é primo.")
