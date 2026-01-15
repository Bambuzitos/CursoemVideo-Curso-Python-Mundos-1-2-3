# Leia um número N e mostre os N primeiros termos da sequência de Fibonacci.

n = int(input("Digite quantos termos da sequência de Fibonacci você quer ver: "))
termo1, termo2 = 0, 1
print("Sequência de Fibonacci:")
for _ in range(n):
    print(termo1, end=' ')
    termo1, termo2 = termo2, termo1 + termo2
print("FIM")