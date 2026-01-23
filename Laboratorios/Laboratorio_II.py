# =====================================================
#   LABORATORIOS – INTRODUCCIÓN A PYTHON (actualización 2025)
#   LABORATORIO II
# =====================================================

# =====================================================
#   EJERCICIO 1
# =====================================================
# 1. Crea un programa que permita ingresar dos cadenas vía la consola y las compare.
#    Luego, debe imprimir un mensaje en caso de que sean iguales y otro en caso
#    de que sean diferentes.

cadena_1 = input("Ingrese texto de la primera cadena: ")
cadena_2 = input("Ingrese texto de la segunda cadena: ")

if cadena_1 == cadena_2:
    print("Ambas cadenas son iguales")
else:
    print("Las cadenas son diferentes")

# 2. Crea un programa que solicite el nombre de un alumno a través de la consola,
#    y luego chequee que no esté vacío. En caso de estarlo, tiene que imprimir
#    un mensaje de error; caso contrario, deberá imprimir un mensaje indicando
#    que se ingresó correctamente.

nombre_alumno = input("Ingrese nombre del alumno: ")

if nombre_alumno == "":
    print("ERROR, debe ingresar nombre del alumno")
else:
    print("Alumno ingresado")

# 3. Pedir la edad por teclado y comparar si es mayor o menor de edad. No olvidar
#    de que para poder comparar el ingreso, debe ser convertido a int, ya que el
#    usuario ingresa un número entero.

edad_usuario = input("Ingrese su edad: ")
edad_usuario = int(edad_usuario)

if edad_usuario >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
    
# =====================================================
#   EJERCICIO 2
# =====================================================
# 1. Con un bucle while, incrementar una variable entera de uno en uno
#    (desde 0 a 10 sin incluir). Mostrar por pantalla el resultado por vuelta.

i = 0

while i < 10:
    print(i)
    i = i + 1

# 2. Pedir por teclado el nombre de usuario. Si está vacío, volver a pedirlo
#    hasta que ingrese un nombre. Luego, saludar al usuario.

nombre_usuario = input("Ingrese su nombre de usuario: ")

while nombre_usuario == "":
    print("ERROR, debe ingresar su nombre de usuario.")
    nombre_usuario = input("Ingrese nuevamente su nombre de usuario: ")

print(f"Buenos días {nombre_usuario}")

# =====================================================
#   EJERCICIO 3
# =====================================================
# Se tiene la siguiente lista de nombres:

# nombres = ["Susana","Alejandro","Roberto"]

# 1. Inserta entre Alejandro y Roberto a Paula, y luego agrega al final a Silvina.

nombres = ["Susana","Alejandro","Roberto"]
nombres.insert(2,"Paula")
nombres.append("Silvina")

# 2. Para finalizar, recorre la lista y muestra a todos los nombres por pantalla.

indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice = indice + 1

# =====================================================
#   EJERCICIO 4
# =====================================================
# Se tiene una lista de nombres:
# nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]

# 1. Recorre la lista con un bucle for.

nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]

for n in nombres:
    print(n)

# =====================================================
#   EJERCICIO 5
# =====================================================
# 1. Crea un programa que solicite una fila y una columna e imprima en pantalla
#    el número en esa posición según la siguiente matriz:
#
#    matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
#
#    Un ejemplo de entrada y salida es el siguiente:
#    Fila: 1
#    Columna: 2
#    6.4
#
#    El resultado es 6.4 porque es el valor ubicado en matriz[1][2].
#
#    El programa debe chequear que la fila y la columna tengan valores válidos.
#    En este caso, las únicas filas válidas son 0 y 1; las columnas, 0, 1 y 2.
#    Si alguno de los dos valores es inválido, debe mostrar un mensaje de error.

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print(matriz)

fila = int(input("Ingrese número de fila: "))
columna = int(input("Ingrese número de columna: "))

if fila < len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("ERROR, debe ingresar una columna correcta")
else:
    print("ERROR, debe ingresar una fila correcta")


# =====================================================
#   EJERCICIO 6
# =====================================================
# 1. Realiza un programa que, ingresando la edad de una persona, determine si es
#    menor, mayor con edad laboral o jubilado (contemplando jubilado para ambos
#    sexos a los 65 años).

edad = input("Ingrese edad:  ")
edad = int(edad)
if edad < 18:
    print("Menor de edad")
else:
    if edad < 65:
        print("Edad laboral")
    else:
        print("Jubilado")

# 2. Se tiene la matriz

#    m = [ [10,50,5], [20,30,70], [15,45,80] ]

#    Recorrela con 2 sentencias for para mostrar cada uno de los elementos que
#    la componen.

m = [ [10,50,5], [20,30,70], [15,45,80] ]

for i in m:
    for j in i:
        print(j)

# =====================================================
#   EJERCICIO 7
# =====================================================
# Una agencia de viajes tiene un sistema de información para paquetes turísticos.
# Realiza un programa que, al ingresar el paquete (solo la letra), genere una
# descripción de lo que contiene cada "combo".
#
# Paquete A: Cancún 7 noches + aéreos: u$s 1200 por persona.
# Paquete B: Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.
# Paquete C: Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.
# Paquete D: Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.

paquete = input("Ingrese el paquete: ")

if paquete =="A" or paquete == "a":
    print("Cancún 7 noches + Aéreos u$s 1200 por persona")
elif paquete == "B" or paquete == "b":
    print("Miami 8 noches + Aéreos + Alquiler de Auto u$s 1500 por persona")
elif paquete == "C" or paquete =="c":
    print("Bariloche 10 noches + Aéreos + excursiones u$s 1300 por persona")
elif paquete == "D" or paquete == "d":
    print("Rio de Janeiro 10 noches + Aéreos + excursiones u$s 1400 por persona")
else:
    print("Error de opción")

# =====================================================
#    FIN DESAFÍO LABORATORIO II
# =====================================================