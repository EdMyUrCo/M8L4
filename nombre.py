def pedir_nombre_valido():
    while True:
        nombre = input("📝 Ingresa tu nombre (1 a 15 caracteres): ").strip()
        if nombre == "":
            print("⚠️ No puedes dejar el nombre en blanco.")
        elif not (1 <= len(nombre) <= 15):
            print("❌ El nombre debe tener entre 1 y 15 caracteres.")
        else:
            return nombre
