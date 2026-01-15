# Jogo par ou ímpar contra o computador. O jogo só para quando o usuário perder. Mostre vitórias consecutivas.

from random import randint
vitorias = 0
while True:
    numero_usuario = int(input("Digite um número: "))
    escolha_usuario = input("Par ou Ímpar? [P/I]: ").strip().upper()
    numero_computador = randint(0, 10)
    total = numero_usuario + numero_computador
    resultado = 'P' if total % 2 == 0 else 'I'
    print(f"Você jogou {numero_usuario} e o computador jogou {numero_computador}. Total de {total} ", end='')
    print("DEU PAR" if resultado == 'P' else "DEU ÍMPAR")
    if escolha_usuario == resultado:
        vitorias += 1
        print("Você VENCEU! Vamos jogar novamente...")
    else:
        print("Você PERDEU!")
        break
print(f"GAME OVER! Você venceu {vitorias} vezes consecutivas.")
