# =====================================================
#   DESAFÍOS – INTRODUCCIÓN A PYTHON (actualización 2025)
#   DESAFÍO DEL MÓDULO I
# =====================================================

# =====================================================
#    EJERCICIO 1
# =====================================================

# 1. Resuelve el siguiente problema utilizando las herramientas aprendidas en el módulo.
# Tomás rindió 3 exámenes y desea saber su promedio a partir de esta información:

# nota_uno = 10
# nota_dos = 6
# nota_tres = 8

# Muestra el promedio por pantalla

nota_uno = 10
nota_dos = 6
nota_tres = 8

promedio = (nota_uno + nota_dos + nota_tres) / 3

print("El promedio de las notas es: ", promedio)

# =====================================================
#    EJERCICIO 2
# =====================================================

# 1. Calcula los minutos que hay en una semana declarando variables.

semana = 1
dias_x_semana = 7
hora_x_dia = 24
minutos_x_hora = 60

minutos_x_semana = semana * dias_x_semana * hora_x_dia * minutos_x_hora

print(f"Hay {minutos_x_semana} minutos en {semana} semana")

# 2. Dada esta situación:Una juguetería tiene mucho éxito en la venta de dos de sus productos: payasos y muñecas. 
# Suele hacer ventas por correo y la empresa de logística les cobra por el peso de cada paquete, por lo que 
# necesitan calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
# muñeca, 75 g.Escribe un programa que:

# ● Solicite al usuario el número de payasos y muñecas vendidos en el último pedido.
# ● Calcule el peso total del paquete que será enviado.

cantidad_munecas = int(input("Ingrese la cantidad de Muñecas del ultimo pedido: "))
cantidad_payasos = int(input("Ingrese la cantidad de payasos del ultimo pedido: "))

peso_muneca = 0.75
peso_payaso = 0.112

peso_total_munecas = cantidad_munecas * peso_muneca

peso_total_payasos = cantidad_payasos * peso_payaso

peso_final = peso_total_munecas + peso_total_payasos

print(":::: DETALLES PESAJE ::::")
print(f"Cantidad de muñecas: {cantidad_munecas} kg" "\n"
      f"Pesaje de muñecas: {peso_muneca} kg" "\n"
      f"Peso total muñecas: {peso_total_munecas}")
print(":::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"Cantidad de payasos: {cantidad_payasos}" "\n"
      f"Pesaje de payasos: {peso_payaso} kg" "\n"
      f"Peso total payasos: {peso_total_payasos} kg")
print(":::::::::::::::::::::::::::::::::::::::::::::::::")
print(f"PESO TOTAL: {peso_final} kls.")

# =====================================================
#    FIN DESAFÍO MÓDULO I
# =====================================================