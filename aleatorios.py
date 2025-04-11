import random

lista = []

for i in range(20):  # Genera 5 números aleatorios
    numero = random.randint(1, 100)  # Números del 1 al 100
    if numero not in lista:
        lista.append(numero)

print(lista)