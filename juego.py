
def calcular_puntos(mano):
    puntos = 0
    ases = 0

    for carta in mano:
        valor = carta["valor"]

        if valor == "A":
            puntos += 11
            ases += 1

        elif valor == "J" or valor == "Q" or valor == "K":
            puntos += 10

        else:
            puntos += int(valor)

    # Ajustar los ases si se superan los 21 puntos
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1

    return puntos


def comprobar_21(mano):
    puntos = calcular_puntos(mano)

    if puntos > 21:
        return "pasado"
    elif puntos == 21:
        return "blackjack"
    else:
        return "continuar"
