from jugador import greet_player, say_goodbye, start_game
from random_num import jugar_adivina_numero
from comprobar import mostrar_mensaje
from nombre import pedir_nombre_valido

def desea_repetir():
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower().strip()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        mostrar_mensaje("advertencia", "Por favor, responde con 's' para sí o 'n' para no.")

def main():
    mostrar_mensaje("info", "¡Bienvenido al juego mágico de adivinanzas intergalácticas!")

    while True:
        nombre = pedir_nombre_valido()
        greet_player(nombre)
        start_game(nombre)
        jugar_adivina_numero(nombre)
        say_goodbye(nombre)

        if not desea_repetir():
            mostrar_mensaje("info", "Juego finalizado. ¡Vuelve pronto!")
            break

if __name__ == "__main__":
    main()
