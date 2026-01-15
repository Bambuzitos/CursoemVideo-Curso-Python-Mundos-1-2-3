# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento do jovem: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    anos_faltando = 18 - idade
    ano_alistamento = ano_atual + anos_faltando
    print(f"Ainda faltam {anos_faltando} anos para o alistamento. O alistamento será em {ano_alistamento}.")    
elif idade == 18:
    print("Está na hora de se alistar ao serviço militar este ano!")
else:
    anos_passados = idade - 18
    ano_alistamento = ano_atual - anos_passados
    print(f"Já se passaram {anos_passados} anos desde o alistamento. O alistamento foi em {ano_alistamento}.")