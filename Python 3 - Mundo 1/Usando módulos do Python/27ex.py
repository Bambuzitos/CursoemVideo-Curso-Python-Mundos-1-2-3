# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite o nome completo de uma pessoa: ").strip()
nomes = nome.split()
print(f"Primeiro nome: {nomes[0]}")
print(f"Último nome: {nomes[-1]}")
