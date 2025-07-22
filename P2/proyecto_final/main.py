import inventario

opcion = True

while opcion:
    print("\n\t...::: Inventario de Maquillaje :::...\n")
    print("\t...::: Sistema de Gestión de Productos :::...\n")
    print(" 1.- Añadir Producto al Inventario")
    print(" 2.- Mostrar Productos del Inventario")
    print(" 3.- Borrar Producto por Código")
    print(" 4.- Modificar Característica de un Producto")
    print(" 5.- Borrar Característica de un Producto")
    print(" 6.- Borrar TODOS los Productos")
    print(" 7.- SALIR")

    opcion_menu = input("\n\tElige una opción: ").strip().upper()

    match opcion_menu:
        case "1":
            inventario.crear_producto()
            inventario.esperarTecla()
        case "2":
            inventario.mostrar_productos()
            inventario.esperarTecla()
        case "3":
            inventario.borrar_producto()
            inventario.esperarTecla()
        case "4":
            inventario.modificar_caracteristica_producto()
            inventario.esperarTecla()
        case "5":
            inventario.borrar_caracteristica_producto()
            inventario.esperarTecla()
        case "6":
            inventario.borrar_todos_productos()
            inventario.esperarTecla()
        case "7":
            opcion = False
            print("\n\tTerminaste la ejecución del programa.")
            inventario.esperarTecla()
        case _:
            print("\n\tOpción inválida, vuelva a intentarlo por favor.")
            inventario.esperarTecla()