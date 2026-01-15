# Crie um programa que faça o computador jogar Jokenpô com você.

from math import e
from random import choice
from time import sleep

opcoes = ["pedra", "papel", "tesoura"]
computador = choice(opcoes)
jogador = input("Escolha pedra, papel ou tesoura: ").lower()
if jogador not in opcoes:
    print("Opção inválida! Escolha pedra, papel ou tesoura.")
    exit()
else:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!")
    if jogador == computador:
        print(f"Empate! Ambos escolheram {jogador}.")
    elif (jogador == "pedra" and computador == "tesoura") or \
        (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
        print(f"Você venceu! {jogador} vence de {computador}.")
    else:
        print(f"Você perdeu! {computador} vence de {jogador}.")
