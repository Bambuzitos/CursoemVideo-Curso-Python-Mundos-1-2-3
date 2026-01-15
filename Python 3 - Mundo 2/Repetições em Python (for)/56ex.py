# Leia nome, idade e sexo de quatro pessoas e mostre:
# - média de idades  
# - nome do homem mais velho  
# - quantas mulheres têm menos de 20 anos

soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ""
quantidade_mulheres_menos_20 = 0
for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    soma_idades += idade
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            quantidade_mulheres_menos_20 += 1
media_idades = soma_idades / 4
print(f"A média de idade do grupo é {media_idades:.1f} anos.")
if nome_homem_mais_velho:
    print(f"O homem mais velho é {nome_homem_mais_velho} com {maior_idade_homem} anos.")
else:
    print("Não há homens no grupo.")
print(f"Ao todo são {quantidade_mulheres_menos_20} mulheres com menos de 20 anos.")