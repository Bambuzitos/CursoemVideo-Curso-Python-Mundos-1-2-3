#  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite alguma coisa: ')
print(f'O tipo dessa variável é : {type(entrada)}')
print(f'Só tem espaços?: {entrada.isspace()}')
print(f'É só número?: {entrada.isnumeric()}')
print(f'É alfabético?: {entrada.isalpha()}')
print(f'É alfanumérico?: {entrada.isalnum()}')
print(f'Está em minusculas? {entrada.islower()}')
print(f'Está em maiuscula? {entrada.isupper()}')
print(f'Está capitalizada?: {entrada.istitle()}')
