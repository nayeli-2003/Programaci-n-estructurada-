from conexion import conectar
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperaTecla():
    input("\n🔘 Oprima cualquier tecla para continuar ...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t🎞 .:: Agregar Películas ::.")
    nombre = input("🎬 Ingresa el nombre: ").upper().strip()

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO peliculas (nombre) VALUES (%s)", (nombre,))
    conexion.commit()
    conexion.close()

    print("\n\t✅ ::: ¡Película guardada en la base de datos! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t📋 .:: Lista de Películas ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    conexion.close()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
    else:
        print("⚠ No hay películas registradas.")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t❌ .:: Eliminar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
        try:
            id_a_eliminar = int(input("\n👉 Ingresa el ID de la película a eliminar: "))
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id_a_eliminar,))
            conexion.commit()
            print("\n✅ ::: Película eliminada.")
        except ValueError:
            print("❌ Entrada inválida.")
    else:
        print("⚠ No hay películas registradas.")
    conexion.close()

def actualizarPeliculas():
    borrarPantalla()
    print("\n\t🔁 .:: Actualizar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()

    if peliculas:
        for peli in peliculas:
            print(f"{peli[0]}. {peli[1]}")
        try:
            id_a_actualizar = int(input("\n👉 Ingresa el ID de la película a actualizar: "))
            nuevo_nombre = input("🎬 Ingresa el nuevo nombre: ").upper().strip()
            cursor.execute("UPDATE peliculas SET nombre = %s WHERE id = %s", (nuevo_nombre, id_a_actualizar))
            conexion.commit()
            print("\n✅ ::: Película actualizada.")
        except ValueError:
            print("❌ Entrada inválida.")
    else:
        print("⚠ No hay películas registradas.")
    conexion.close()

def buscarPeliculas():
    borrarPantalla()
    print("\n\t🔍 .:: Buscar Película ::.")

    conexion = conectar()
    cursor = conexion.cursor()
    busqueda = input("🔎 Ingresa parte del nombre a buscar: ").upper().strip()
    cursor.execute("SELECT id, nombre FROM peliculas WHERE nombre LIKE %s", ('%' + busqueda + '%',))
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print("\n🎯 Resultados encontrados:")
        for peli in resultados:
            print(f"{peli[0]}. {peli[1]}")
    else:
        print("❌ No se encontraron coincidencias.")

def vaciarPelicula():
    borrarPantalla()
    print("\n\t🧹 .:: Vaciar Lista de Películas ::.")
    confirmacion = input("¿Estás seguro que deseas borrar todas las películas? (si/no): ").lower()
    if confirmacion == "si":
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM peliculas")
        conexion.commit()
        conexion.close()
        print("✅ Todas las películas fueron eliminadas.")
    else:
        print("⏹ Operación cancelada.")