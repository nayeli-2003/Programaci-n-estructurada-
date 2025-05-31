'''
List (Array)
son colleciones o conjunto de datos de datos/valores bajo un mismo 
nombre, para acceder alos valores se hace con un indice
numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite
miembros duplicados
"
'''

import os
os.system("cls")

#Funciones más comunes en las listas

paises=["Mexico ", "Canada", "Brasil", "España"]

numeros=[23,12,100,34]

varios=["Hola",True,33,3.12]

#Ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort() 
print(numeros)
paises.sort()
print(paises.sort)

#Agregar o insertar o añadir un elemento a la lista 
#1er forma ("Mexico ", "Canada", "Brasil", "España")
print(paises)
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1, "Honduras")
print(paises)

#Eligir o borrar o suprimir un elemento a la lista 
#1er forma 
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma de borrar 
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de una lista
#1er forma ("Mexico ", "Canada", "Brasil", "España")

print("Brasil" in paises)

#Contar el numero de veces que un elemento esta dentro de una lista
#23,12,100,34
print(numeros)
numeros. count(12)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(12))

#Dar la vuelta de los elemntos de una lista
print(numeros)
print(paises)
paises.reverse()
numeros.reverse()
print(numeros)
print(paises)

#Conocer el indice o la posicion de un valor de la lista
print(paises.index("España"))

#Unir el contenido de 2 o mas listas en una sola
#numeros(100,34,23,12,12)
numeros2=[300,500,100]

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)