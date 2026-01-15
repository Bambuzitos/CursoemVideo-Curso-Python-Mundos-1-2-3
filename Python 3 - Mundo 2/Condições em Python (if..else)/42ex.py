# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print("Digite o comprimento de três retas para verificar se podem formar um triângulo.")
reta1 = float(input("Comprimento da primeira reta: "))
reta2 = float(input("Comprimento da segunda reta: "))
reta3 = float(input("Comprimento da terceira reta: "))
if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print("As retas podem formar um triângulo.", end=' ')
    if reta1 == reta2 == reta3:
        print("Tipo do triângulo: EQUILÁTERO.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("Tipo do triângulo: ISÓSCELES.")
    else:
        print("Tipo do triângulo: ESCALENO.")