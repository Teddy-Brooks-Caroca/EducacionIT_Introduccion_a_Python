# =====================================================
#   PROYECTO INTEGRADOR - ETAPA 3
#   SISTEMA CON DICCIONARIOS Y OPCIONES MEJORADAS
# =====================================================

# =====================================================
#   CONSIGNA GENERAL
# =====================================================
# La lista de alumnos creada en el módulo anterior ahora debe ser un diccionario,
# en donde las claves serán nombres de alumnos y los valores sus respectivas 
# cantidades de cursos.
#
# Menú actualizado:
# 1 - Añadir un alumno a la lista.
# 2 - Ver la lista de alumnos.
# 3 - Ver cantidad de cursos.
# 4 - Salir.
#
# Para esto se debe modificar el código de las opciones 1 y 2 (agregar un nuevo 
# alumno y ver la lista de alumnos).
#
# ● Usando prompts de inteligencia artificial, debes optimizar el código.
#
# La tercera opción será “Ver la cantidad de cursos de un alumno”. Deberá 
# solicitar el nombre de un alumno e imprimir en pantalla el número de cursos 
# que tiene asociados como clave. La cuarta opción es la de salir, como en la 
# versión anterior.

# =====================================================
#   ESPECIFICACIONES DE LAS OPCIONES
# =====================================================
# OPCIÓN 1: Añadir un alumno
# - Solicitar nombre del alumno y cantidad de cursos
# - Almacenarlos en un diccionario donde:
#   clave = nombre del alumno (string)
#   valor = cantidad de cursos (entero)
#
# OPCIÓN 2: Ver la lista de alumnos
# - Recorrer el diccionario y mostrar todos los alumnos con sus respectivos cursos
# - Formato sugerido: "Nombre - X cursos"
#
# OPCIÓN 3: Ver cantidad de cursos de un alumno específico
# - Solicitar el nombre de un alumno
# - Buscar en el diccionario y mostrar la cantidad de cursos asociada
# - Si el alumno no existe, mostrar mensaje apropiado
#
# OPCIÓN 4: Salir
# - Salir del sistema con mensaje de despedida
#
# MEJORA REQUERIDA: Optimizar el código usando prompts de IA para hacerlo
# más eficiente, legible y mantenible.

usuario = input("Ingrese nombre de usuario: ")

contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    print("Credenciales correctas. Bienvenido al sistema.")
    

    diccionario_alumnos = {}
    
    while True:
        
        print("Ingrese el número de la operación que desea ejecutar:")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Ver cantidad de cursos de un alumno.")
        print("4 - Salir.")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            cantidad_cursos = input("Ingrese la cantidad de cursos: ")
            cantidad_cursos = int(cantidad_cursos)
            diccionario_alumnos[nombre_alumno] = cantidad_cursos
            print("¡El alumno fue añadido a la lista!")
        
        
        elif opcion == "2":
            print("Lista de alumnos:")
            for nombre, cursos in diccionario_alumnos.items():
                print(nombre + " - " + str(cursos) + " cursos")
                
        
        elif opcion == "3":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            if nombre_alumno in diccionario_alumnos:
                print(nombre_alumno + " tiene " +  str(diccionario_alumnos[nombre_alumno]) + " cursos.")
            else:
                print("El alumno no existe en la lista.")
        
        
        elif opcion == "4":
            print("¡Gracias por utilizar el programa!")
            break  
        
        else:
            print("Opción no válida. Intente de nuevo.")
else:
    print("Usuario y/o contraseña incorrecta.")

# =====================================================
#    CÓDIGO OPTIMIZADO
# =====================================================

def mostrar_menu():
    print("\nIngrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Ver cantidad de cursos de un alumno.")
    print("4 - Salir.")


usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    print("Credenciales correctas. Bienvenido al sistema.")

    alumnos = {}

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            cursos = int(input("Ingrese la cantidad de cursos: "))
            alumnos[nombre] = cursos
            print("¡El alumno fue añadido a la lista!")

        elif opcion == "2":
            if alumnos:
                print("Lista de alumnos:")
                for nombre, cursos in alumnos.items():
                    print(f"{nombre} - {cursos} cursos")
            else:
                print("No hay alumnos cargados.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno: ")
            if nombre in alumnos:
                print(f"{nombre} tiene {alumnos[nombre]} cursos.")
            else:
                print("El alumno no existe en la lista.")

        elif opcion == "4":
            print("¡Gracias por utilizar el programa!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

else:
    print("Usuario y/o contraseña incorrecta.")

# ===========================================================================================
#    Se optimizó el código separando responsabilidades mediante funciones, mejorando 
# la legibilidad, reduciendo repetición de código y facilitando su mantenimiento, manteniendo 
# un nivel introductorio sin estructuras avanzadas.
# ===========================================================================================
# =====================================================
#    FIN ETAPA 3 - PROYECTO INTEGRADOR
# =====================================================