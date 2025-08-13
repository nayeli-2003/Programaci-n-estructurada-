def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")
 
def esperarTecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def mostrar_menu_inicio():
    print("\n \t.:: Sistema de Gestión de Inventario ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion

def menu_usuario_logueado(id_usuario, nombre, email):
    print(f"\n\tBienvenido {nombre} ({email})")
    print("\n \t.:: Sistema de Gestión de Productos y Más ::.. \n\t\t1.-  Agregar Productos  \n\t\t2.-  Agregar Proveedores \n\t\t3.- Agregar Categoría \n\t\t4.- SALIR ")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion

def menu_productos():
    print("\n \t .::  Menú de Productos ::. \n\t1.- Agregar Productos \n\t2.- Mostrar Productos \n\t3.- Modificar Producto \n\t4.- Borrar Productos \n\t5.- SALIR")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion

def menu_proveedores():
    print("\n \t .::  Menú de Proveedores ::. \n\t1.- Agregar Proveedores \n\t2.- Mostrar Proveedores \n\t3.- Modificar Proveedores \n\t4.- Borrar Proveedores \n\t5.- SALIR")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion

def menu_categoria():
    print("\n \t .::  Menú de Categoría ::. \n\t1.- Agregar Categoría \n\t2.- Mostrar Categorías \n\t3.- Borrar Categorías \n\t4.- SALIR")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion