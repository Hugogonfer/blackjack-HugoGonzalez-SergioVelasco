# Mostrar el menú principal
def mostrar_menu():
    print("\n===== BLACKJACK =====")
    print("1. Jugar")
    print("2. Salir")

    while True:
        opcion = input("Elige una opcion: ")

        if opcion == "1" or opcion == "2":
            return opcion

        print("Opcion incorrecta. Intentalo de nuevo.")


# Mostrar un mensaje de bienvenida
def mostrar_bienvenida():
    print("========================")
    print("  BIENVENIDO AL BLACKJACK")
    print("========================")
    print("El objetivo es acercarse a 21 sin pasarse.")
    print("Juegas contra la banca.\n")


# Mostrar las cartas de una mano
def mostrar_cartas(mano, nombre):
    print("\nCartas de", nombre + ":")

    for carta in mano:
        print("-", carta["valor"], "de", carta["palo"])


# Mostrar la puntuacion de una mano
def mostrar_puntuacion(nombre, puntos):
    print("Puntuacion de", nombre + ":", puntos)


# Preguntar si el jugador quiere otra carta
def pedir_decision():
    while True:
        print("\n1. Pedir carta")
        print("2. Plantarse")

        opcion = input("Elige una opcion: ")

        if opcion == "1" or opcion == "2":
            return opcion

        print("Opcion incorrecta. Intentalo de nuevo.")


# Mostrar el resultado de la partida
def mostrar_resultado(resultado):
    print("\n===== RESULTADO =====")

    if resultado == "jugador":
        print("¡Has ganado la partida!")
    elif resultado == "banca":
        print("La banca ha ganado.")
    elif resultado == "empate":
        print("La partida ha terminado en empate.")
    else:
        print("Resultado desconocido.")


# Preguntar si se quiere jugar otra partida
def jugar_otra_vez():
    while True:
        respuesta = input("\n¿Quieres jugar otra partida? (s/n): ").lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False

        print("Introduce 's' o 'n'.")


# Mostrar mensaje de despedida
def mostrar_despedida():
    print("\n¡Gracias por jugar al Blackjack!")