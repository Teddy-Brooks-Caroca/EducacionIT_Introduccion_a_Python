# =====================================================
#   DESAFÍOS – INTRODUCCIÓN A PYTHON 
#   DESAFÍO DEL MÓDULO IV
# =====================================================

# =====================================================
#   EJERCICIO 1: MULTIPLICAR LISTA
# =====================================================
# Escribe una función que sirva para multiplicar cada elemento de una lista
# numérica por un valor (ambos deben ser parámetros de función); y devuelva
# la nueva lista con cada elemento en su respectiva posición, pero ya multiplicado.

def multiplicar(lista,valor):
    nueva = []
    for n in lista:
        resultado = n * valor
        nueva.append(resultado)
    return nueva

numeros = [10,5,3,20]
m = 5
print(multiplicar(numeros,m))

# =====================================================
#   EJERCICIO 2: SEPARAR PARES E IMPARES
# =====================================================
# Desarrolla una función que reciba una lista con números enteros y devuelva
# en una matriz:
#
# ● Como primer elemento, una lista con los números pares.
# ● Como segundo elemento, una lista de los números impares de la lista recibida.
#
# Idea: [pares, impares]

def parimpar(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return [pares,impares]

valores = [10,11,12,13,14,15,16]
print(parimpar(valores))


# =====================================================
#   EJERCICIO 3: DADO CON INTERFAZ GRÁFICA
# =====================================================
# Crea una aplicación de escritorio que simule un dado, es decir, debe arrojar
# número aleatorio de 1 al 6.
#
# ● La vista de la aplicación debería ser similar a la imagen de la derecha.
# ● En la caja, deberían de aparecer los resultados aleatorios cada vez que se
#   presiona el botón.
# ● Antes de mostrar los resultados se limpia la caja, dejando el mismo resultado
#   hasta que se vuelve a pulsar.
#
# Ayuda para tkinter:
# - caja.delete(0, tk.END)  → limpia la caja
# - caja.insert(0, variable) → inserta el valor en la caja

import tkinter as tk
import random

def arrojar():
    caja.delete(0,tk.END)
    valor = random.randint(1,6)
    caja.insert(0,valor)

ventana = tk.Tk()
ventana.config(width=220,height=200)
ventana.title("Dado 2.0")
boton = tk.Button(text="Arrojar el dado",command=arrojar)
boton.place(x=60,y=40,width=100,height=50)
etq = tk.Label(text="Valor: ")
etq.place(x=60,y=110)
caja = tk.Entry()
caja.place(x=60,y=140,width=100)
ventana.mainloop()

# =====================================================
#    FIN DESAFÍO DEL MÓDULO IV
# =====================================================