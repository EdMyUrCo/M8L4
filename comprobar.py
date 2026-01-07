def mostrar_mensaje(tipo, mensaje):
    tipo = tipo.lower()
    if tipo == "info":
        print(f"\n🔹 INFO: {mensaje}")
    elif tipo == "advertencia":
        print(f"\n⚠️ ADVERTENCIA: {mensaje}")
    elif tipo == "error":
        print(f"\n❌ ERROR: {mensaje}")
    elif tipo == "exito":
        print(f"\n✅ ÉXITO: {mensaje}")
    else:
        print(f"\n{mensaje}")
