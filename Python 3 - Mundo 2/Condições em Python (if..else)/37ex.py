# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Sua opção: "))  
if opcao == 1:
    convertido = bin(numero)[2:]
    print(f"O número {numero} em binário é {convertido}.")
elif opcao == 2:
    convertido = oct(numero)[2:]
    print(f"O número {numero} em octal é {convertido}.")
elif opcao == 3:
    convertido = hex(numero)[2:].upper()
    print(f"O número {numero} em hexadecimal é {convertido}.")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")