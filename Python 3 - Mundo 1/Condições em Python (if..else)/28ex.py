# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
numero_computador = randint(0, 5)
numero_usuario = int(input("Tente adivinhar o número que o computador escolheu entre 0 e 5: "))
print("PROCESSANDO...")
if numero_usuario == numero_computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! O número escolhido pelo computador foi {numero_computador}.")
