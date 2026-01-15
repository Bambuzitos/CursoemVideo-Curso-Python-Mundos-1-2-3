# Melhore o jogo de adivinhação até o jogador acertar. Conte os palpites.

from random import randint
numero_secreto = randint(1, 100)
palpites = 0
while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    palpites += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {palpites} palpites.")
        break