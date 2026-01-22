# =====================================================
#   PROYECTO INTEGRADOR - ETAPA 1
#   SISTEMA DE GESTIÓN DE ALUMNOS Y CURSOS
# =====================================================

# =====================================================
#   CONSIGNA GENERAL
# =====================================================
# Una universidad desea crear un programa para contabilizar los cursos 
# que tiene cada alumno. Para ello, se debe realizar primero una aplicación 
# de consola donde solo puede manejar el usuario con nombre "admin" y 
# contraseña "uni123".
#
# Una vez ingresado al sistema, debe aparecer un menú de opciones para:
# - Dar de alta nuevos alumnos con la cantidad de cursos
# - Ver listados
# - Ver cursos por alumnos
#
# Para finalizar, el sistema se debe mostrar en una interfaz gráfica.

# =====================================================
#   EJERCICIO 1
# =====================================================
# Crea un programa que solicite el nombre de un alumno a través de la 
# consola y la cantidad de cursos, y luego muestre por pantalla esa información.
#
# Ejemplo:
# Ingrese su nombre: Mateo
# Ingrese la cantidad de cursos: 3
#
# Salida:
# Mateo está inscripto en 3 cursos

nombre_alumno = input("Ingrese nombre y apellido del alumno: ")
cantidad_cursos = int(input("Ingrese cantidad de cursos del alumno: "))

print(f"El alumno {nombre_alumno} está inscripto en {cantidad_cursos} cursos")

# =====================================================
#    FIN ETAPA 1 - PROYECTO INTEGRADOR
# =====================================================