

contra="python2025"
entrada=""
intentos=0

while entrada!=contra and intentos < 3:
    entrada=input("ingrese el password: ")
    if entrada != contra:
        print("incorrecto!!")
    intentos +=1

if entrada==contra:
    print("Correcto")
else:
    print("Agoto los intentos")