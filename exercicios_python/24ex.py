# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input("Digite o nome da cidade: ").strip()
comeca_com_santo = cidade.upper().startswith("SANTO")
if comeca_com_santo:
    print(f"A cidade {cidade} começa com 'SANTO'.")
else:
    print(f"A cidade {cidade} não começa com 'SANTO'.")