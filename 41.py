#41.Escribir un programa que nos muestre si es hora de desayunar, almorzar, merendar o
# cenar dependiendo de la hora ingresada, según el siguiente listado.
# 10 Desayuno
# 13 Almuerzo
# 17 Merienda
# 21 cena
hora=int(input("ingrese horario "))
if   hora>=10 and hora<13:
	print("desayuno")
elif hora>=13 and hora<17:
	print("almuesrzo ")
elif hora>=17 and hora<21:
	print("merienda")
elif hora>=21 and hora<=24:
	print("cena")
else:
	print(" fuera de rango")
