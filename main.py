from cartas import crear_baraja, mezclar_baraja, repartir_carta
from juego import calcular_puntos, jugar_banca, determinar_ganador
from interfaz import (
    mostrar_bienvenida,
    mostrar_menu,
    mostrar_cartas,
    mostrar_puntuacion,
    pedir_decision,
    mostrar_resultado,
    jugar_otra_vez,
    mostrar_despedida
)


def jugar_partida():
    baraja = crear_baraja()
    mezclar_baraja(baraja)

    jugador = []
    banca = []

    for i in range(2):
        jugador.append(repartir_carta(baraja))
        banca.append(repartir_carta(baraja))

    mostrar_cartas(jugador, "Jugador")
    mostrar_puntuacion("Jugador", calcular_puntos(jugador))

    mostrar_cartas(banca[:1], "Banca")

    # Turno del jugador
    while calcular_puntos(jugador) < 21:
        decision = pedir_decision()

        if decision == "1":
            carta = repartir_carta(baraja)
            jugador.append(carta)

            mostrar_cartas(jugador, "Jugador")
            mostrar_puntuacion("Jugador", calcular_puntos(jugador))

        elif decision == "2":
            print("\nTe has plantado.")
            break

    puntos_jugador = calcular_puntos(jugador)

    if puntos_jugador > 21:
        print("\nTe has pasado de 21.")

    elif puntos_jugador == 21:
        print("\nHas conseguido 21 puntos.")

    # Turno de la banca
    if puntos_jugador <= 21:
        jugar_banca(banca, baraja)

    # Mostrar las cartas finales
    print("\n===== FIN DE LA PARTIDA =====")

    mostrar_cartas(jugador, "Jugador")
    mostrar_puntuacion("Jugador", calcular_puntos(jugador))

    mostrar_cartas(banca, "Banca")
    mostrar_puntuacion("Banca", calcular_puntos(banca))

    # Determinar el ganador
    resultado = determinar_ganador(jugador, banca)
    mostrar_resultado(resultado)


def main():
    mostrar_bienvenida()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            jugar_partida()

            if not jugar_otra_vez():
                break

        elif opcion == "2":
            break

    mostrar_despedida()


if __name__ == "__main__":
    main()