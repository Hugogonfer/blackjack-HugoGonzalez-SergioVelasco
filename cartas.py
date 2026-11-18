

import random

# Crear una baraja de 52 cartas
def crear_baraja():
    palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    baraja = []

    for palo in palos:
        for valor in valores:
            carta = {
                "valor": valor,
                "palo": palo
            }
            baraja.append(carta)

    return baraja


# Mezclar las cartas de la baraja
def mezclar_baraja(baraja):
    random.shuffle(baraja)


# Repartir una carta de la baraja
def repartir_carta(baraja):
    if len(baraja) > 0:
        return baraja.pop()
    return None
