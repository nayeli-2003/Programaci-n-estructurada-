inventario = []

def borra_pantalla():
    import os
    os.system("cls")
    
def esperarTecla():
    input("\n\t... Oprime una tecla para continuar...")

def crear_producto():
    """Agrega un nuevo producto al inventario."""
    global inventario
    borra_pantalla()
    print("\n\t.:: Alta de Productos ::.\n")
    producto = {
        "descripcion": input("Ingrese la descripcion: ").strip(),
        "marca": input("Ingrese la marca: ").strip(),
        "precio": input("Ingrese el precio: ").strip(),
        "cantidad": input("Ingrese la cantidad: ").strip(),
        "codigo": input("Ingrese el codigo: ").strip().upper()
    }
    inventario.append(producto)
    print("\n\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")
    esperarTecla()

def mostrar_productos():
    """Muestra todos los productos registrados."""
    borra_pantalla()
    print("\n\t.:: Mostrar los Productos ::.")
    if len(inventario) > 0:
        for i in range(len(inventario)):
            producto = inventario[i]
            print(f"\nProducto #{i+1}")
            for clave, valor in producto.items():
                print(f"{clave}: {valor}")
    else:
        print("\n\t.:: No hay productos en este momento en el Sistema ::.")
    esperarTecla()

def borrar_producto():
    """Elimina un producto por su código."""
    global inventario
    borra_pantalla()
    print("\n\t.:: Borrar un producto por código ::.\n")
    codigo = input("Ingrese el código del producto a borrar: ").strip().upper()
    for producto in inventario:
        if producto["codigo"] == codigo:
            inventario.remove(producto)
            print("\n\t.:: ¡Producto eliminado con éxito! ::.")
            break
    else:
        print("\n\t.:: ¡No se encontró un producto con ese código! ::.")
    esperarTecla()

def borrar_todos_productos():
    """Elimina todos los productos del inventario."""
    global inventario
    borra_pantalla()
    print("\n\t.:: Borrar TODOS los productos ::.\n")
    resp = input("¿Deseas borrar todos los productos? (si/No): ").lower().strip()
    if resp == "si":
        inventario.clear()
        print("\n\t.:: ¡Todos los productos han sido eliminados! ::.")
    else:
        print("\n\t.:: No se borraron los productos. ::.")
    esperarTecla()

def modificar_caracteristica_producto():
    """Modifica una característica de un producto."""
    global inventario
    borra_pantalla()
    print("\n\t.:: Modificar Característica de un Producto ::.\n")
    codigo = input("Ingrese el código del producto a modificar: ").strip().upper()
    for producto in inventario:
        if producto["codigo"] == codigo:
            atributo = input("Ingrese la característica a modificar: ").lower().strip()
            if atributo in producto:
                nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").strip()
                producto[atributo] = nuevo_valor
                print(f"\n\t.:: ¡La característica '{atributo}' se ha modificado con éxito! ::.\n")
            else:
                print(f"\n\t.:: ¡La característica '{atributo}' no existe! ::.\n")
            break
    else:
        print("\n\t.:: ¡No se encontró un producto con ese código! ::.")
    esperarTecla()

def borrar_caracteristica_producto():
    """Elimina una característica específica de un producto."""
    global inventario
    borra_pantalla()
    print("\n\t.:: Borrar Característica de un Producto ::.\n")
    codigo = input("Ingrese el código del producto: ").strip().upper()
    for producto in inventario:
        if producto["codigo"] == codigo:
            atributo = input("Ingrese la característica a borrar: ").lower().strip()
            if atributo in producto:
                del producto[atributo]
                print(f"\n\t.:: ¡La característica '{atributo}' se ha borrado con éxito! ::.\n")
            else:
                print(f"\n\t.:: ¡La característica '{atributo}' no existe! ::.\n")
            break
    else:
        print("\n\t.:: ¡No se encontró un producto con ese código! ::.")
    esperarTecla()