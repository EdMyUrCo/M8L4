import random
from comprobar import mostrar_mensaje

def jugar_adivina_numero(nombre):
    numero_secreto = random.randint(1, 10)
    adivinado = False

    for intento in range(1, 4):
        try:
            intento_usuario = int(input(f"\n🔢 Intento {intento}/3 - Adivina un número del 1 al 10: "))
        except ValueError:
            mostrar_mensaje("error", "Por favor, ingresa un número válido.")
            continue

        if intento_usuario == numero_secreto:
            if intento == 1:
                mostrar_mensaje("exito", f"🌟 ¡Increíble, {nombre}! ¡Lo adivinaste a la primera!")
            else:
                mostrar_mensaje("exito", f"¡Felicidades, {nombre}! Adivinaste el número.")
            adivinado = True
            break
        else:
            mostrar_mensaje("advertencia", f"No es el número, {nombre}. Te quedan {3 - intento} intento(s).")

    if not adivinado:
        mostrar_mensaje("error", f"¡Oh no, {nombre}! El número correcto era: {numero_secreto}")
