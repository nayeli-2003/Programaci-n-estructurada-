"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#1.- funcion que no reciben parametros y no regresan valor
def solicitarDatos1():
    nombre=input("Nomnbre: ")
    telefono=input("Telefono:")
    print(f"Nombre: {nombre} y su telefono: {telefono}")

#3.- funcion que reciben parametros y no regresa valor
def solicitardatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"Nombre: {nombre} y su telefono: {telefono}")

#2.- funcion que no reciben parametros y regresa valor
def solicitarDatos2():
    nombre=input("Nomnbre: ")
    telefono=input("Telefono:")
    return nombre, telefono

#4.- funcion que reciben parametros y regresa valor
def solicitarDatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre, telefono 

#Mandar llamar o invocar las funciones

solicitarDatos1()

nombre=input("Escribe el nombre: ")
telefono=input("Escribe el telefono: ")
solicitardatos3(nombre, telefono)

num,tel=solicitarDatos2()
print(f"\t\nLos datos son de la agenda son:\n Nombre: {nombre}\n Telefono: {tel}") 

nombre=input("Escribe el nombre: ")
telefono=input("Escribe el telefono: ")
nom,tel=solicitarDatos4(nombre,telefono)
print(f"\t\nLos datos de la Agenda son:\n Nombre: {nom}\n Telefono:{tel}")
