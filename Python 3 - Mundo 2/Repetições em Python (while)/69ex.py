# Leia idade e sexo de várias pessoas e mostre:
# maiores de 18  
# quantas mulheres  
# quantas mulheres com menos de 20  

maiores_de_18 = 0
quantidade_mulheres = 0
quantidade_mulheres_menos_20 = 0
while True:
    print("----- NOVA PESSOA -----")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    if idade > 18:
        maiores_de_18 += 1
    if sexo == 'F':
        quantidade_mulheres += 1
        if idade < 20:
            quantidade_mulheres_menos_20 += 1
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break
print(f"Ao todo temos {maiores_de_18} pessoas maiores de 18 anos.")
print(f"Ao todo temos {quantidade_mulheres} mulheres cadastradas.")
print(f"Ao todo temos {quantidade_mulheres_menos_20} mulheres com menos de 20 anos.")