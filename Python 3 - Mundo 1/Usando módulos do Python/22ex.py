#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome_completo = input("Digite o nome completo: ").strip()
nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()
letras_sem_espacos = len(nome_completo.replace(" ", ""))
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print(f"Nome em maiúsculas: {nome_maiusculo}")
print(f"Nome em minúsculas: {nome_minusculo}")
print(f"Número total de letras (sem espaços): {letras_sem_espacos}")
print(f"Número de letras no primeiro nome: {letras_primeiro_nome}")
