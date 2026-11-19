
from cartas import repartir_carta


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


def jugar_banca(banca, baraja):
    while calcular_puntos(banca) < 17:
        carta = repartir_carta(baraja)

        if carta is None:
            break

        banca.append(carta)

    return banca


def determinar_ganador(jugador, banca):
    puntos_jugador = calcular_puntos(jugador)
    puntos_banca = calcular_puntos(banca)

    if puntos_jugador > 21:
        return "banca"

    if puntos_banca > 21:
        return "jugador"

    if puntos_jugador > puntos_banca:
        return "jugador"

    if puntos_banca > puntos_jugador:
        return "banca"

    return "empate"
