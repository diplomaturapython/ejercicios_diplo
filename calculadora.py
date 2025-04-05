'''
a = float(input("Número 1: "))
b = float(input("Número 2: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", a + b)
elif operacion == "-":
    print("Resultado:", a - b)
elif operacion == "*":
    print("Resultado:", a * b)
elif operacion == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: división entre cero.")
else:
    print("Operación no válida.")

'''
#while condicion:

contador = 0

#while contador < 5:
#    print(contador)
#    contador+=1

while True:
    print(contador)
    contador+=1
    if contador==5:
        break