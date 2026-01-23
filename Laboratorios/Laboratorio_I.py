# =====================================================
#   LABORATORIOS – INTRODUCCIÓN A PYTHON (actualización 2025)
#   LABORATORIO I
# =====================================================

# =====================================================
#   EJERCICIO 1
# =====================================================
# 1. Arma una frase con las 3 variables dadas y muéstrala por pantalla.
# 
# texto_uno = "potente"
# texto_dos = "sol"
# texto_tres = "triunfo"
#
# Es obligatorio usar las 3 variables, pero también puedes agregar palabras 
# para generar una frase. No importa el orden que elijas para las variables.

texto_uno = "potente"
texto_dos = "sol"
texto_tres = "triunfo"

print(f"La {texto_uno} luz del {texto_dos} irradió en {texto_tres}")

# 2. Realiza un programa que tenga 2 variables, base = 10 y altura = 5.
#    Calcula el área de un rectángulo y muestra el resultado por pantalla.

base = 10
altura = 5

area_rectangulo = base * altura

print(f"El área del rectángulo es: {area_rectangulo} cms.")

# 3. Dadas 2 variables: a = 20 y b = 10, muestra por pantalla su suma,
#    resta, multiplicación y división.

a = 20
b = 10

suma = a + b
resta = a - b
mult = a * b
div = a / b

print(":::: RESULTADOS ::::")
print(f"{a} + {b} = {suma}" "\n"
      f"{a} - {b} = {resta}" "\n"
      f"{a} * {b} = {mult}" "\n"
      f"{a} / {b} = {div}")
print(":::::::::::::::::::::")

# =====================================================
#   EJERCICIO 2
# =====================================================
# 1. En un script de Python, crea:
#
# - 3 variables nombradas a, b y c con valores numéricos cualesquiera.
# - 1 variable llamada resultado, que sea la suma de las primeras tres.
#
# Imprime en pantalla cada una de ellas. Antes de mostrar el valor de cada
# variable, indica su nombre en una línea anterior.
#
# Este es un ejemplo de lo que se debería mostrar en pantalla:
#
# a:
# 5
# b:
# 7
# c:
# 10
# resultado:
# 22

a = 8
b = 15
c = 78

resultado = a + b + c

print("a:")
print(a)
print("b:")
print(b)
print("c:")
print(c)
print("resultado:")
print(resultado)

# =====================================================
#   EJERCICIO 3
# =====================================================
# 1. Crea 2 variables, saludo y nombre, cuyos contenidos sean "Hola, " en el 
#    primer caso y tu nombre en el segundo. Intenta sumarlas con el operador +.
#    Muestra el resultado en pantalla.
#
#    Para guardar el resultado de la suma, puedes crear una tercera variable.

saludo = "Hola, "
nombre = "Leo"

resultado = saludo + nombre

print(resultado)

# =====================================================
#    FIN DESAFÍO LABORATORIO I
# =====================================================