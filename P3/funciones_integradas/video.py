mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]

mi_lista = [1, 2, 3]
mi_lista.insert(1, 5)
print(mi_lista)  # Salida: [1, 5, 2, 3]

mi_lista = [1, 2, 3]
otra_lista = [4, 5]
mi_lista.extend(otra_lista)
print(mi_lista)  # Salida: [1, 2, 3, 4, 5]

mi_lista = [1, 2, 3, 2]
mi_lista.remove(2)
print(mi_lista)  # Salida: [1, 3, 2]

mi_lista = [1, 2, 3]
elemento_eliminado = mi_lista.pop(1)
print(mi_lista)  # Salida: [1, 3]
print(elemento_eliminado)  # Salida: 2

mi_lista = [1, 2, 3, 2]
indice = mi_lista.index(2)
print(indice)  # Salida: 1

mi_lista = [1, 2, 3, 2]
conteo = mi_lista.count(2)
print(conteo)  # Salida: 2

mi_lista = [3, 1, 2]
mi_lista.sort()
print(mi_lista)  # Salida: [1, 2, 3]

mi_lista = [1, 2, 3]
mi_lista.reverse()
print(mi_lista)  # Salida: [3, 2, 1]

mi_lista = [1, 2, 3]
mi_lista.clear()
print(mi_lista)  # Salida: []

mi_lista = [1, 2, 3]
copia_lista = mi_lista.copy()
print(copia_lista)  # Salida: [1, 2, 3]