# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite um valor em metros: "))
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros} m equivalem a {decimetros:g} dm, {centimetros:g} cm e {milimetros:g} mm.")

decametro = metros / 10
hectometro = metros / 100
quilometro = metros / 1000
print(f"{metros} m equivalem a {decametro:g} dam, {hectometro:g} hm e {quilometro:g} km.")