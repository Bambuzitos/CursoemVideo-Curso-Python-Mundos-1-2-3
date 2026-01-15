# Mostre um menu com operações entre dois valores:
# somar  
# multiplicar  
# maior  
# novos números  
# sair 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print(f"A soma de {num1} + {num2} é {num1 + num2}.")
    elif opcao == 2:
        print(f"O produto de {num1} x {num2} é {num1 * num2}.")
    elif opcao == 3:
        if num1 > num2:
            print(f"O maior número é {num1}.")
        elif num2 > num1:
            print(f"O maior número é {num2}.")
        else:
            print("Os dois números são iguais.")
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")
print("Programa encerrado. Até mais!")


