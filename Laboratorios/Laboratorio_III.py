# =====================================================
#   LABORATORIOS – INTRODUCCIÓN A PYTHON (actualización 2025)
#   LABORATORIO III - FUNCIONES
# =====================================================

# =====================================================
#   EJERCICIO 1: ESTRELLAS
# =====================================================
# Escribe una función mostrar_estrellas(cantidad) que muestre tantos * como
# indica cantidad, comenzando con un *.
#
# Por ejemplo:
# mostrar_estrellas(5)
#
# Salida:
# *
# **
# ***
# ****
# *****

def estrellas(cantidad):
    for n in range(1, cantidad + 1):
        print("*" * n)

estrellas(5)

# =====================================================
#   EJERCICIO 2: SUMAR CON UNA FUNCIÓN
# =====================================================
# Crea una función que tome 2 números como argumentos y retorne el resultado.
#
# Por ejemplo, el código: sumar(10,30). Debe retornar: 40.

def sumar(a,b):
    c = a + b
    print(c)

sumar(10,30)

# =====================================================
#   EJERCICIO 3: GENERAR UN RANGO CON UNA FUNCIÓN
# =====================================================
# Crea una función rango(desde, hasta, intervalo) que retorne una lista de números,
# tal como la función incorporada range(), aunque según el intervalo especificado.
#
# Por ejemplo, el siguiente código:
# lista = rango(1, 10, 2)
# print(lista)
# Debe imprimir: [1, 3, 5, 7, 9], puesto que se genera una lista desde 1 hasta 10
# con un intervalo de 2.
#
# Tomar como base el código de la función rango() que se encuentra en el material
# del alumno.

def rango(desde,hasta,intervalo):
    lista_numeros = []
    while desde < hasta:
        lista_numeros.append(desde)
        desde = desde + intervalo
    return lista_numeros

lista = rango(1,8,2)

print(lista)

# =====================================================
#   EJERCICIO 4: PALÍNDROMO
# =====================================================
# Crea una función que devuelva Verdadero si una lista de elementos es palíndroma
# (se lee igual en un sentido que en otro). En caso contrario, debe devolver Falso.
#
# Por ejemplo:
# es_palindromo([3, 2, 3]) → True
# es_palindromo(["m", 2, 2, "m"]) → True

l1 = ["m", 2, 1, 2, "m"]

def es_palindromo(lista):
    pos_izq = 0
    pos_der = len(lista) - 1
    
    while pos_der >= pos_izq:
        if lista[pos_izq] != lista[pos_der]:
            return False
        pos_izq = pos_izq + 1
        pos_der = pos_der - 1
    return True

print(es_palindromo(l1))
      
# =====================================================
#    FIN DESAFÍO LABORATORIO III
# =====================================================