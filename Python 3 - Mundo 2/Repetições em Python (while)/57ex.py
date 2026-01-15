# Leia o sexo de uma pessoa aceitando apenas M ou F. Repita até ser válido.

sexo = ""
while sexo not in ['M', 'F']:
    sexo = input("Digite o sexo [M/F]: ").strip().upper()
    if sexo not in ['M', 'F']:
        print("Dados inválidos. Por favor, digite M ou F.")
print(f"Sexo {sexo} registrado com sucesso.")