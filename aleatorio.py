import random
secreto=random.randint(1,10)
adivino=False

while not adivino:
    intento=int(input("Adivine el numero(1-10):"))

    if intento==secreto:
        print("Es correcto")
        adivino=True
    else:
        print("Siga participando!!!")
