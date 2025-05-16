#Escribir un programa que permita que permita ingresar una nota numérica entre 1 y 10
# (Agregue la validación de números o caracteres válidos)·
#Nota entre 1 y 3	Desaprobó
#Nota entre 4 y 6	Aprobó
#Nota 7 o más	Promocionó


def nota():
	nota_alumno=int(input(" ingrese nota "))
	return  nota_alumno




def validacion():
	nota_recibida=nota()
	if nota_recibida>=1 and nota_recibida<=3:
		print(" desaprobado")
	elif nota_recibida>=4 and nota_recibida<=6:
		print(" aprobo")
	elif nota_recibida>=7 and nota_recibida<=10:
		print(" promociono ")
	else:print(" opcion incorrecta valor no contemplado ")


validacion()