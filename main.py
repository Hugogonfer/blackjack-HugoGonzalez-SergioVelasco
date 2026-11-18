from interfaz import mostrar_bienvenida, mostrar_menu


def jugar_partida():
    # Todavía vacía: se rellena en los siguientes commits
    print("Partida en construcción...")


def main():
    mostrar_bienvenida()

    # Bucle principal: se repite hasta que el usuario elija salir
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            break  # Salimos del bucle

    print("\nGracias por jugar al Blackjack.")


# Solo se ejecuta si lanzamos este archivo directamente
if __name__ == "__main__":
    main()