# =====================================================
#   LABORATORIOS – INTRODUCCIÓN A PYTHON (actualización 2025)
#   LABORATORIO IV - MÓDULOS, INTERFAZ Y JUEGOS
# =====================================================

# =====================================================
#   EJERCICIO 1: GENERAR UN RANGO CON UNA FUNCIÓN
# =====================================================
# Crea una función rango(desde, hasta, intervalo) que retorne una lista de números,
# tal como la función incorporada range(), aunque según el intervalo especificado.
#
# Por ejemplo, el siguiente código:
# lista = rango(1, 10, 2)
# print(lista)
# debe imprimir: [1, 3, 5, 7, 9]
#
# Puesto que se genera una lista desde 1 hasta 10 con un intervalo de 2.
#
# NOTA: No puedes usar la función range() para resolver este ejercicio.

def rango(desde, hasta, intervalo):
    numeros = []
    while desde < hasta:
        numeros.append(desde)
        desde = desde + intervalo
    return numeros

desde = int(input("Ingrese número de inicio de secuencia: "))
hasta = int(input("Ingrese número de fin de secuencia: "))
intervalo = int(input("Ingrese el intervalo de la secuencia: "))

lista = rango(desde, hasta, intervalo)
print(lista)

# =====================================================
#   EJERCICIO 2: CONTADOR TEMPORIZADOR
# =====================================================
# Realiza un script contador de 0 hasta 10, que vaya mostrando los números
# segundo a segundo.

import time
i = 0
while i < 10:
    print(i)
    time.sleep(1)
    i = i + 1

# =====================================================
#   EJERCICIO 3: DADO
# =====================================================
# Genera un programa de consola que tenga un menú y permita generar números
# aleatorios entre 1 y 6, como si fuera un dado.
#
# El “Menú” debe contener las opciones:
# 1. Tirar dado.
# 2. Salir

import random
while True:
    print("Menú")
    print("1 - Tirar dado")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        valor = random.randint(1,6)
        print("El valor del dado es:", valor)
    elif opcion == "2":
        print(" ¡Gracias por usar nuestro programa! ")
        break
    else:
        print("¡No existe esa opción!")

# =====================================================
#   EJERCICIO 4: CALCULADORA
# =====================================================
# Crea una aplicación de escritorio con dos cajas de texto y un botón, de modo que
# al presionarlo se imprima en pantalla la suma de los dos números ingresados
# en las primeras.
#
# La disposición de los controles y el tamaño de la ventana quedan a tu criterio.

import tkinter as tk


def convertir(dato):
    if dato.isdecimal():
        dato = int(dato)
    else:
        dato = "error"
    return dato

def sumar():
    a = caja_a.get()
    a = convertir(a)
    b = caja_b.get()
    b = convertir(b)
    if a != "error" and b!="error":
        print(a + b)
    else:
        print("No se puede realizar")

ventana = tk.Tk()
ventana.config(width=250, height=200)
ventana.title("Ejemplo")
caja_a = tk.Entry()
caja_a.place(x=20, y=20, width=50, height=25)
caja_b = tk.Entry()
caja_b.place(x=20, y=60, width=50, height=25)
boton = tk.Button(text="Sumar", command=sumar)
boton.place(x=20, y=100)
ventana.mainloop()


# =====================================================
#   EJERCICIO 5: ADIVINAR NÚMEROS
# =====================================================
# Escribe un programa donde el usuario debe adivinar un número oculto (generado
# aleatoriamente) en un rango entre 10 y 40, en 5 intentos.
#
# Opcional: El programa puede guiar al usuario indicando si el número es mayor
# o menor.

intentos = 0
numero = random.randint(10, 40)

print("Debe ingresar un número entre 10 y 40.")

while intentos < 5:
    ingreso = int(input("Intenta adivinar: "))
    intentos += 1

    if ingreso == numero:
        print(f"¡Has adivinado en {intentos} intentos!")
        break
    elif ingreso < numero:
        print("Tu número es menor.")
    else:
        print("Tu número es mayor.")

if ingreso != numero:
    print(f"No adivinaste. El número era {numero}.")

# =====================================================
#   EJERCICIO 6: LISTA DE NÚMEROS ALEATORIOS
# =====================================================
# Haz una lista que contenga 10 números aleatorios entre 10 y 50. En pantalla
# deben aparecer los números separados por un guión medio.
#
# Puedes guiarte con el ejemplo de la derecha.


cantidad = 0
lista_numeros = []
while cantidad < 10:
    numero_aleat = random.randint(10, 50)
    lista_numeros.append(numero_aleat)
    cantidad = cantidad + 1

texto_final = ''
for numero in lista_numeros:
    texto_final = texto_final + str(numero) + " - "
print(texto_final)

# =====================================================
#    FIN DESAFÍO LABORATORIO IV
# =====================================================