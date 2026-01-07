def pedir_nombre_limitado():
    while True:
        nombre = input("Ingresa tu nombre (1 a 15 caracteres): ").strip()
        if not nombre:
            print("⚠️ El nombre no puede estar vacío.")
        elif 1 <= len(nombre) <= 15:
            return nombre
        else:
            print("❌ El nombre debe tener entre 1 y 15 caracteres.")
