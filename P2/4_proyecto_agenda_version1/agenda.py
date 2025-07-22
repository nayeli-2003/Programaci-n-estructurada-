def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def menu_principal():
    print("\n\t.:: Agenda de Contactos ::.\n")
    print("1️⃣.- Agregar contacto")
    print("2️⃣.- Mostrar todos los contactos")
    print("3️⃣.- Buscar contacto por nombre")
    print("4️⃣.- Salir")
    return input("\nElige una opción (1-4): ").strip()

def agregar_contacto(datos):
    borrarPantalla()
    print("\n\t.:: Agregar Contacto ::.\n")
    nombre = input("Nombre: ").strip().title()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    datos.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    print("\nContacto agregado con éxito.")

def mostrar_todos_los_contactos(datos):
    borrarPantalla()
    print("\n\t.:: Lista de Contactos ::.\n")
    if datos:
        for i, contacto in enumerate(datos, 1):
            print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    else:
        print("No hay contactos registrados.")

def buscar_contacto_por_nombre(datos):
    borrarPantalla()
    print("\n\t.:: Buscar Contacto ::.\n")
    nombre_buscar = input("Ingresa el nombre a buscar: ").strip().title()
    encontrados = [c for c in datos if c['nombre'] == nombre_buscar]
    if encontrados:
        for contacto in encontrados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    else:
        print("No se encontró ningún contacto con ese nombre.")