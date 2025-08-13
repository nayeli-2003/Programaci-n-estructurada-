import funciones
import conexionBD
from usuarios import usuarios
from categorias import categorias
from productos import producto
from proveedores import proveedores
import getpass

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.mostrar_menu_inicio().strip().upper()

        if opcion == "1" or opcion == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t..:: Registro en el Sistema ::..")
            nombre = input("\t¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\tIngresa tu email: ").lower().strip()
            password = getpass.getpass("\tIngresa tu contraseña: ").strip()
            confirmar = getpass.getpass("\tConfirma tu contraseña: ").strip()

            if not nombre or not apellidos or not email or not password:
                print("\n\tTodos los campos son obligatorios.")
            elif password != confirmar:
                print("\n\tLas contraseñas no coinciden.")
            else:
                lista_usuario = usuarios.registrar(nombre, apellidos, email, password)
                if lista_usuario:
                    print(f"\n\t{nombre} {apellidos} se registró correctamente con el email {email}")
                else:
                    print("\n\tNo es posible registrar el usuario, inténtalo más tarde.")
            funciones.esperarTecla()

        elif opcion == "2" or opcion == "LOGIN":
            funciones.borrarPantalla()
            print("\n\t..:: Inicio de Sesión ::..")
            email = input("\tIngresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\tIngresa tu contraseña: ").strip()
            lista_usuario = usuarios.inicio_sesion(email, password)
            if lista_usuario:
                menu_usuario_logueado_principal(lista_usuario[0], lista_usuario[1], lista_usuario[2])
            else:
                print("\n\tE-mail y/o contraseña incorrectos. Verifica y vuelve a intentar.")
                funciones.esperarTecla()

        elif opcion == "3" or opcion == "SALIR":
            print("\n\tTerminó la ejecución del sistema")
            opcion = False
            funciones.esperarTecla()

        else:
            print("\n\tOpción no válida")
            funciones.esperarTecla()

def menu_usuario_logueado_principal(usuario_id, nombre_usuario, apellidos):
    productos = []
    proveedores = []
    categorias = []

    while True:
        funciones.borrarPantalla()
        print(f"\n\tBienvenido {nombre_usuario} {apellidos}")
        opcion = funciones.menu_usuario_logueado(usuario_id, nombre_usuario, apellidos)

        if opcion == "1":
            while True:
                funciones.borrarPantalla()
                opcion_producto = funciones.menu_productos()

                if opcion_producto == "1":
                    nombre_producto = input("\n\tNombre del producto: ").strip()
                    try:
                        precio = float(input("\tPrecio: ").strip())
                        cantidad = int(input("\tCantidad: ").strip())
                        producto_nuevo = {"nombre": nombre_producto, "precio": precio, "cantidad": cantidad}
                        productos.append(producto_nuevo)
                        print("\t✅ Producto agregado con éxito.")
                    except ValueError:
                        print("\t❌ Precio o cantidad inválidos.")
                    funciones.esperarTecla()

                elif opcion_producto == "2":
                    if not productos:
                        print("\n\t📦 No hay productos registrados.")
                    else:
                        print("\n\t📋 Lista de productos:")
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")
                    funciones.esperarTecla()

                elif opcion_producto == "3":
                    if not productos:
                        print("\n\t📦 No hay productos para modificar.")
                    else:
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")
                        try:
                            indice = int(input("\n\tNúmero del producto a modificar: ")) - 1
                            if 0 <= indice < len(productos):
                                productos[indice]["nombre"] = input("\tNuevo nombre: ").strip()
                                productos[indice]["precio"] = float(input("\tNuevo precio: ").strip())
                                productos[indice]["cantidad"] = int(input("\tNueva cantidad: ").strip())
                                print("\t✏️ Producto modificado.")
                            else:
                                print("\t❌ Número inválido.")
                        except ValueError:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_producto == "4":
                    if not productos:
                        print("\n\t📦 No hay productos para borrar.")
                    else:
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")
                        try:
                            indice = int(input("\n\tNúmero del producto a borrar: ")) - 1
                            if 0 <= indice < len(productos):
                                eliminado = productos.pop(indice)
                                print(f"\t🗑️ Producto '{eliminado['nombre']}' eliminado.")
                            else:
                                print("\t❌ Número inválido.")
                        except ValueError:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_producto == "5":
                    break

                else:
                    print("\n\t❌ Opción inválida.")
                    funciones.esperarTecla()

        elif opcion == "2":
            while True:
                funciones.borrarPantalla()
                opcion_prov = funciones.menu_proveedores()

                if opcion_prov == "1":
                    nombre = input("\n\tNombre del proveedor: ").strip()
                    telefono = input("\tTeléfono: ").strip()
                    email = input("\tCorreo electrónico: ").strip()
                    prov = {"nombre": nombre, "telefono": telefono, "email": email}
                    proveedores.append(prov)
                    print("\t✅ Proveedor agregado correctamente.")
                    funciones.esperarTecla()

                elif opcion_prov == "2":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores registrados.")
                    else:
                        print("\n\t📋 Lista de proveedores:")
                        for i, p in enumerate(proveedores, start=1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Teléfono: {p['telefono']}, Email: {p['email']}")
                    funciones.esperarTecla()

                elif opcion_prov == "3":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores para modificar.")
                    else:
                        for i, p in enumerate(proveedores, 1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Teléfono: {p['telefono']}, Email: {p['email']}")
                        try:
                            idx = int(input("\n\tNúmero del proveedor a modificar: ")) - 1
                            if 0 <= idx < len(proveedores):
                                proveedores[idx]["nombre"] = input("\tNuevo nombre: ").strip()
                                proveedores[idx]["telefono"] = input("\tNuevo teléfono: ").strip()
                                proveedores[idx]["email"] = input("\tNuevo correo: ").strip()
                                print("\t✏️ Proveedor modificado.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada inválida.")
                    funciones.esperarTecla()

                elif opcion_prov == "4":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores para borrar.")
                    else:
                        for i, p in enumerate(proveedores, 1):
                            print(f"\t{i}. Nombre: {p['nombre']}, Teléfono: {p['telefono']}, Email: {p['email']}")
                        try:
                            idx = int(input("\n\tNúmero del proveedor a eliminar: ")) - 1
                            if 0 <= idx < len(proveedores):
                                eliminado = proveedores.pop(idx)
                                print(f"\t🗑️ Proveedor '{eliminado['nombre']}' eliminado.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_prov == "5":
                    break

                else:
                    print("\n\t❌ Opción no válida.")
                    funciones.esperarTecla()

        elif opcion == "3":
            while True:
                funciones.borrarPantalla()
                opcion_cat = funciones.menu_categoria()

                if opcion_cat == "1":
                    nombre = input("\n\tNombre de la categoría: ").strip()
                    categorias.append(nombre)
                    print(f"\t✅ Categoría '{nombre}' agregada con éxito.")
                    funciones.esperarTecla()

                elif opcion_cat == "2":
                    if not categorias:
                        print("\n\t📂 No hay categorías registradas.")
                    else:
                        print("\n\t📋 Lista de categorías:")
                        for i, cat in enumerate(categorias, start=1):
                            print(f"\t{i}. {cat}")
                    funciones.esperarTecla()

                elif opcion_cat == "3":
                    if not categorias:
                        print("\n\t📂 No hay categorías para borrar.")
                    else:
                        print("\n\t📋 Categorías disponibles:")
                        for i, cat in enumerate(categorias, start=1):
                            print(f"\t{i}. {cat}")
                        try:
                            idx = int(input("\n\tNúmero de la categoría a eliminar: ")) - 1
                            if 0 <= idx < len(categorias):
                                eliminado = categorias.pop(idx)
                                print(f"\t🗑️ Categoría '{eliminado}' eliminada.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_cat == "4":
                    break

                else:
                    print("\n\t❌ Opción inválida.")
                    funciones.esperarTecla()

        elif opcion == "4":
            print("\n\t👋 Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("\n\t❌ Opción inválida.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()