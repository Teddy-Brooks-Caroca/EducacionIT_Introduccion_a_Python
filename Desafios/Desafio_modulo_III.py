# =====================================================
#   DESAFÍOS – INTRODUCCIÓN A PYTHON 
#   DESAFÍO DEL MÓDULO III
# =====================================================

# =====================================================
#   EJERCICIO 1: FUNCIÓN PARA FORZAR EL INGRESO NUMÉRICO
# =====================================================
# Crea una función que fuerce el ingreso de solo números.
#
# ● Debe recibir un número por argumento y verificar que este sea un número
#   posible de convertir a int.
# ● En caso contrario, volver a pedir el ingreso dentro de la función.
# ● Deberá retornar el valor convertido a int.

def comprobar_valor(valor):
    while valor.isdecimal() == False:
        print("Error, no corresponde a un número.")
        valor = input("Ingrese el valor nuevamente: ")
    valor = int(valor)
    return(valor)

valor = input("Ingrese un valor: ")

valor = comprobar_valor(valor)

print(f"El valor ingresado {valor} corresponde a un número.") 

# =====================================================
#   EJERCICIO 2: FUNCIÓN ÁREA DEL RECTÁNGULO
# =====================================================
# Realizar una función llamada area_rectangulo que reciba la base y la altura
# por argumento, y que devuelva (retorne) el área del rectángulo.

def area_rectangulo(base,altura):
    area = base * altura
    return(area)

base = int(input("Ingrese base del rectangulo: "))

altura = int(input("Ingrese altura del rectangulo: "))

print(f"AREA DE RECTANGULO: {area_rectangulo(base,altura)}")

# =====================================================
#    FIN DESAFÍO DEL MÓDULO III
# =====================================================