# Contagem regressiva de 10 até 0 com pausa de 1 segundo.

from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("Feliz Ano Novo!")
