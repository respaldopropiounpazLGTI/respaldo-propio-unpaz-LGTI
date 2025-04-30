#34. Escribir un programa que permita que permita ingresar una nota numérica entre 1 y
# 10,(utilizar 3 condicionales simples).Si la nota está entre 1 y 3 # desaprobó
# Si la nota está entre 4 y 6 # aprobó .
# Si la nota es 7 o más # promociono
nota=float(input(" ingrese nota "))
if nota >=1 and nota <=3:
	print(" desaprobo ")
elif nota>=4 and nota <=6:
	print(" aprobo ")
elif nota >=7 and nota <=10:
	print(" promociono ")
else:print(" valor incorrecto  ")


