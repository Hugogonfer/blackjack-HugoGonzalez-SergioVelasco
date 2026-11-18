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
