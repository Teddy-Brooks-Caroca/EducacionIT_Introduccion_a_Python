# =====================================================
#   PROYECTO INTEGRADOR - ETAPA 2
#   SISTEMA DE GESTIÓN CON MENÚ INTERACTIVO
# =====================================================

# =====================================================
#   CONSIGNA GENERAL
# =====================================================
# Continúa el desarrollo del código incluyendo estos requisitos:
#
# a. Para ingresar al menú, solicitar nombre de usuario y contraseña. 
#    Solo si el usuario es "admin" y la contraseña es "uni123", se muestra 
#    el menú. De lo contrario, se indica "Usuario y/o contraseña incorrecta".
#
#    Ejemplo:
#    Ingrese nombre de usuario: admin
#    Ingrese la contraseña: uni123
#
# b. Una vez ingresado, mostrar el siguiente menú:
#
#    Ingrese el número de la operación que desea ejecutar:
#    1 - Añadir un alumno a la lista.
#    2 - Ver la lista de alumnos.
#    3 - Salir.
#
#    El sistema debe pedir una opción infinitamente hasta que el usuario escriba "3".

# =====================================================
#   ESPECIFICACIONES DE LAS OPCIONES
# =====================================================
# OPCIÓN 1:
# Si se presiona 1, debe solicitar el nombre de un alumno y la cantidad de 
# cursos en la que se encuentra inscripto.
#
# Estos dos valores deben almacenarse como una lista de dos elementos 
# (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.
#
# Ejemplo:
# Ingrese el nombre del alumno: Pablo
# Ingrese la cantidad de cursos: 3
# ¡El alumno fue añadido a la lista!
#
# OPCIÓN 2:
# Si se presiona 2, recorrer la lista de alumnos y mostrar por pantalla.
#
# Ejemplo:
# Lista de alumnos:
# Pablo - 3 cursos
#
# OPCIÓN 3:
# Si presiona 3, saludar al usuario y salir del sistema.
#
# Ejemplo:
# ¡Gracias por utilizar el programa!
#
# OPCIÓN INVÁLIDA:
# Si el usuario presiona cualquier otro número, se debe informar que la 
# opción no es correcta y volver a mostrar el menú.
#
# Ejemplo:
# La opción ingresada no es correcta, vuelva a intentarlo.

lista_alumnos = []

usuario = input("Ingrese su rol de usuario: ")

clave = input("Ingrese su clave: ")

if usuario == "admin" and clave == "uni123":
    print("Credenciales son correctas.")
    
    while True:

        print("Ingrese el número de la operación que desea ejecutar")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":

            nombre_alumno = input("Ingrese nombre del alumno: ")
            cantidad_cursos = int (input("Ingrese cantidad de cursos: "))

            lista_alumnos.append([nombre_alumno,cantidad_cursos])

            print(f"El/La alumno/a {nombre_alumno} fue añadido/a a la lista.")
    
        elif opcion == "2":

            if lista_alumnos:
                print("Lista de alumnos:")
                for alumno in lista_alumnos:
                    print(f"El/La alumno/a {alumno[0]} tiene {alumno[1]}")
            else:
                print("No hay alumnos en la lista.")
        
        elif opcion == "3":

            print("Gracias por utilizar el programa.")
            break

        else:
            print("Ingrese una de las opciones válidas. Intente de nuevo.")

else:
    print("Usuario o contraseña incorrectos.")

# =====================================================
#    FIN ETAPA 2 - PROYECTO INTEGRADOR
# =====================================================