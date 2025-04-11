'''
# FORMA 1
semaforo_parpadea = True      # P
tiempo_menor_5_seg = True     # S
calle_menor_10_metros = True  # M
no_llevo_peso = True          # C
no_hay_autos_peligrosos = False # A

# Evaluar si se puede cruzar
puedo_cruzar = (
    semaforo_parpadea and
    tiempo_menor_5_seg and
    calle_menor_10_metros and
    no_llevo_peso and
    no_hay_autos_peligrosos
)

# Resultado
if puedo_cruzar:
    print("Cruzo la calle.")
else:
    print("No cruzo, espero.")
'''

#Forma 2
def puedo_cruzar(semaforo, tiempo, calle, sin_peso, sin_autos):
    if semaforo and tiempo and calle and sin_peso and sin_autos:
        return True
    else:
        return False


if puedo_cruzar(True, True, True, True, False):
    print("Cruzo la calle.")
else:
    print("No cruzo.")

