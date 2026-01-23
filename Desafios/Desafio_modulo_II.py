# =====================================================
#   DESAFÍOS – INTRODUCCIÓN A PYTHON 
#   DESAFÍO DEL MÓDULO II
# =====================================================

# =====================================================
#   EJERCICIO 1
# =====================================================
# Crea un programa para estudiantes que cumpla con esta tarea: cada alumno
# debe ingresar su nota y, de acuerdo con eso, el sistema debe mostrar un
# mensaje que diga:
#
# - "Excelente" si la nota es un 10.
# - "Muy bien" si está entre 7 y 9.
# - "Bien" si está entre un 4 y un 6.
# - "Mal" si está entre 0 y 3.
# - Si la nota no corresponde a ninguno de estos valores, mostrar 
#   "La nota ingresada es incorrecta".

nota_alumno = int(input("Ingrese su nota: "))

if nota_alumno == 10:
    print("Excelente")
elif nota_alumno >= 7 and nota_alumno <= 9:
    print("Muy bien")
elif nota_alumno >= 4 and nota_alumno <= 6:
    print("Bien")
elif nota_alumno >= 0 and nota_alumno <= 3:
    print("Mal")
else:
    print("La nota ingresada es incorrecta")

# =====================================================
#   EJERCICIO 2
# =====================================================
# Desarrolla un programa que cumpla los siguientes pasos:
#
# 1. Se preguntará el tipo de rol que desempeña una persona en una institución
#    por una entrada del tipo input. Los valores posibles son “admin” o “profesor”.
#
# 2. Luego, si la persona es “admin” o “profesor”, se debería pedir la contraseña,
#    siendo la única válida “1234” (la contraseña se toma como string).
#
# 3. Si la contraseña ingresada es válida, se pedirá el nombre de la persona,
#    y si no es vacío, se la saludará.
#
# Contemplar los casos donde no se cumple como corresponde y mostrar un
# mensaje en pantalla.

rol = input("Ingrese rol que desempeña: ")

if rol == "admin" or "profesor":
    clave = input("Ingrese su calve: ")
    if clave == "1234":
        nombre = input("Ingrese su nombre:")
        if nombre == "":
            print("Debe ingresar su nombre.")
        else:
            print(f"Buenos días {nombre}.")
    else:
        print("Ha ingresado una clave errónea.")
else:
    print("No se considera rol.")

# =====================================================
#   EJERCICIO 3
# =====================================================
# 1. Lee la siguiente situación problemática:
#    Un empleado cobró 300 dólares por mes desde enero a junio, 500 dólares
#    de julio a octubre, y 700 dólares por mes en noviembre y en diciembre.
#
# 2. Crea un programa que calcule el sueldo promedio y que indique si este
#    empleado está cobrando un sueldo bajo, normal o mejor de lo normal.
#
#    ● Sueldo bajo: por debajo de 300 dólares.
#    ● Sueldo normal: entre 300 a 900.
#    ● Sueldo mejor de lo normal: más de 900 dólares.

primer_tramo = 300 * 6
segundo_tramo = 500 * 4
tercer_tramo = 700 * 2

promedio_sueldo = (primer_tramo + segundo_tramo + tercer_tramo) / 3

print(f"Su sueldo promedio es: {promedio_sueldo}")

if promedio_sueldo <= 300:
    print("Su sueldo es bajo")
elif promedio_sueldo > 300 and promedio_sueldo <= 900:
    print("Su sueldo es normal")
else:
    print("Su sueldo es mejor de lo normal")

# =====================================================
#   EJERCICIO 4
# =====================================================
# A la derecha, vemos un diagrama de flujo de cómo se hace para calcular un
# año bisiesto. La idea es llevar este algoritmo a código Python.
'''
                ┌─────────────────┐
                │  Ingresar año   │
                └────────┬────────┘
                         │
                        ▼
               ┌─────────────────┐
               │ ¿Es divisible   │
               │     por 4?      │
               └────────┬────────┘
                        │
               ┌───────┴────────┐
           No  │                │  Sí
               ▼                ▼
      ┌─────────────┐   ┌─────────────────┐
      │ NO BISIESTO │   │ ¿Es divisible   │
      └─────────────┘   │     por 100?    │
                        └────────┬────────┘
                                 │
                        ┌───────┴────────┐
                    No  │                │  Sí
                        ▼                ▼
               ┌─────────────┐   ┌─────────────────┐
               │   BISIESTO  │   │ ¿Es divisible   │
               └─────────────┘   │     por 400?    │
                                 └────────┬────────┘
                                          │
                                 ┌───────┴────────┐
                             No  │                │  Sí
                                 ▼                ▼
                        ┌─────────────┐   ┌─────────────┐
                        │ NO BISIESTO │   │   BISIESTO  │
                        └─────────────┘   └─────────────┘
'''

a = input("Ingrese año: ")
a = int(a)
if a % 400 == 0:
    print("Es bisiesto")
else:
    if a % 4 == 0 and a % 100 != 0 :
        print("Es bisiesto")
    else:
        print("No es bisiesto")
print("Fin")

# =====================================================
#   EJERCICIO 5
# =====================================================
# Escribe un programa que permita crear una lista de nombres.
#
# Para ello, el programa debe pedir un número y luego solicitar esa cantidad
# de nombres para crear la lista. Por último, el programa tiene que mostrar
# la lista creada.

cantidad = input("¿Cuantos nombres desea ingresar?: ")

cantidad = int(cantidad)

nombres = []

contador = 0

while contador < cantidad:
    name = input("Ingrese un nombre: ")
    nombres.append(name)
    contador = contador + 1

print(nombres)

# =====================================================
#    FIN DESAFÍO DEL MÓDULO II
# =====================================================