# Leia ano de nascimento de sete pessoas e diga quantas são maiores de idade.

from datetime import date
ano_atual = date.today().year
maiores = 0
for _ in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
print(f"Ao todo tivemos {maiores} pessoas maiores de idade.")
print(f"E também tivemos {7 - maiores} pessoas menores de idade.")
