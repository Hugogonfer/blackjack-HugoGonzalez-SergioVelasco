from cartas import crear_baraja, mezclar_baraja, repartir_carta
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
    mostrar_cartas(banca[:1], "Banca")

    while True:
        decision = pedir_decision()

        if decision == "1":
            carta = repartir_carta(baraja)
            jugador.append(carta)

            print("\nHas recibido otra carta.")
            mostrar_cartas(jugador, "Jugador")

        elif decision == "2":
            print("\nTe has plantado.")
            break

    print("\n===== FIN DEL TURNO =====")
    mostrar_cartas(jugador, "Jugador")
    mostrar_cartas(banca, "Banca")

    # Pendiente de integrar juego.py:
    # calcular_puntos()
    # jugar_banca()
    # determinar_ganador()


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