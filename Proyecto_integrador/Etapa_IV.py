# =====================================================
#   PROYECTO INTEGRADOR - ETAPA 4
#   INTERFAZ GRÁFICA DE ESCRITORIO
# =====================================================

# =====================================================
#   CONSIGNA GENERAL
# =====================================================
# 1. Migra las tres funcionalidades del programa (agregar alumno, ver la cantidad
#    de cursos de un alumno y ver la lista completa) a una aplicación de escritorio.
#    La información se seguirá mostrando en la consola.
#
# 2. Con botones se debe poder ver la lista de alumnos, agregar un nuevo alumno,
#    ver cantidad de cursos y salir.
#
# ● El botón “Ver lista de alumnos” debe mostrar la lista de los alumnos en la consola.
#
# ● “Agregar a la lista” debe agregar un nuevo alumno al diccionario con el nombre
#   y la cantidad de cursos ingresados en las cajas de texto correspondientes.
#
# ● “Ver cantidad de cursos” debe mostrar el número de cursos asociados al nombre
#   ingresado en la primera caja de texto.
#
# ● El programa debe incluir funcionalidad para salir.
#
# Estructura visual sugerida (ver imagen en PDF):
# - Título: "Proyecto integrador"
# - Botón: "Ver lista de alumnos"
# - Campo: "Nombre alumno:" (caja de texto)
# - Campo: "Cursos:" (caja de texto)
# - Botón: "Agregar a la lista"
# - Botón: "Ver cantidad de cursos"
#
# Emplea todo lo aprendido en el curso. El programa no debe de terminar de
# forma imprevista a causa de un error.

# =====================================================
#   ESPECIFICACIONES TÉCNICAS
# =====================================================
# - Usar tkinter para la interfaz gráfica
# - Mantener el diccionario de alumnos (clave: nombre, valor: cursos)
# - Validar entradas (nombres no vacíos, cursos como números enteros)
# - Manejar errores (alumno no encontrado, entrada inválida)
# - Mostrar resultados en consola según lo solicitado
# - Diseño libre pero funcional

import tkinter as tk

def validar_nombre(nombre):
    if nombre == "":
        return "error"
    return nombre

def validar_cursos(cursos):
    if cursos.isdecimal():
        return int(cursos)
    else:
        return "error"

def ver_lista():
    print("Lista de alumnos:")
    if alumnos == {}:
        print("No hay alumnos cargados.")
    else:
        for nombre in alumnos:
            print(nombre, "-", alumnos[nombre], "cursos")

def agregar_alumno():
    nombre = caja_nombre.get()
    cursos = caja_cursos.get()

    nombre = validar_nombre(nombre)
    cursos = validar_cursos(cursos)

    if nombre == "error":
        print("Error: el nombre no puede estar vacío.")
    elif cursos == "error":
        print("Error: los cursos deben ser un número entero.")
    else:
        alumnos[nombre] = cursos
        print("Alumno agregado correctamente.")

def ver_cantidad_cursos():
    nombre = caja_nombre.get()

    if nombre == "":
        print("Error: ingrese un nombre.")
    elif nombre in alumnos:
        print(nombre, "tiene", alumnos[nombre], "cursos.")
    else:
        print("El alumno no existe.")

def salir():
    ventana.destroy()

alumnos = {}

ventana = tk.Tk()
ventana.title("Proyecto integrador")
ventana.geometry("400x300")

boton_lista = tk.Button(ventana, text="Ver lista de alumnos", command=ver_lista)
boton_lista.place(x=10, y=10)

etiqueta_nombre = tk.Label(ventana, text="Nombre alumno:")
etiqueta_nombre.place(x=10, y=60)

caja_nombre = tk.Entry(ventana)
caja_nombre.place(x=120, y=60, width=200)

etiqueta_cursos = tk.Label(ventana, text="Cursos:")
etiqueta_cursos.place(x=10, y=100)

caja_cursos = tk.Entry(ventana)
caja_cursos.place(x=120, y=100, width=50)

boton_agregar = tk.Button(ventana, text="Agregar a la lista", command=agregar_alumno)
boton_agregar.place(x=10, y=150)

boton_ver_cursos = tk.Button(ventana, text="Ver cantidad de cursos", command=ver_cantidad_cursos)
boton_ver_cursos.place(x=150, y=150)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.place(x=10, y=200)

ventana.mainloop()

# =====================================================
#    FIN ETAPA 4 - PROYECTO INTEGRADOR
# =====================================================