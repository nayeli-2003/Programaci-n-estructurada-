import os
#Ejemplo 1:Crear una lista de numeros e impimir el contenido
os.system("cls")
numeros = [10, 20, 30, 40, 50]
print("numeros")

#2da forma
for i in numeros:
    print(i)

#3ra forma
for i in range(0,len(numeros)):
    print(numeros[i])

#Ejemplo 2:Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

os.system("cls")

palabras=("hola, mundo, si")

palabras_buscar=input("Dame la palabra a buscar: ")

#1ra forma
if palabras_buscar in palabras:
    print(f"Se encontro la palabra")
else:
    print("No se encontro la palabra")

#2da forma
encontro=False 
for i in palabras:
    if i == palabras_buscar:
        encontro=True
if encontro==True:        
        print("Se encontro la palabra")
else:
        print("No se encontro la palabra")

#3era forma
encontro=False 
for i in range(0,len(numeros)):
    if palabras [i] == palabras_buscar:
        encontro=True

if encontro:        
        print("Se encontro la palabra")
else:
        print("No se encontro la palabra")


#Añadir elementos a una lista

numeros=[]
opc="si"
while opc=="si":
     numero=float(input("Dame un numero entero o decimal:"))
     opc=input("¿Desea solicitar otro numero? (si/no): ").lower()

print("numeros")



#Crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas

os.system("cls")
agenda = [
["Carlos", "618826826"],
[ "Juan", "618826826"],
[ "Maria", "618826826"],
   ]
print (agenda)

for r  in agenda:
    print(r)


for r in agenda:
    print(r)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c] )
valores = ""
for r in range(0,3):
    for c in range(0,2):
        valores+=f"{agenda[r][c]}, "
    valores+= f"\n"
print(valores)





