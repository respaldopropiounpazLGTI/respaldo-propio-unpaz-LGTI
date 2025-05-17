#Escribir un programa que pregunte al usuario por el número de horas trabajadas y
#el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


def cuenta():
	horas_trabajadas=int(input(" ingrese horas trabajadas "))
	precio=int(input(" ingrese precio por hora "))
	sueldo=horas_trabajadas*precio
	print("el sueldo es :",sueldo)
	
cuenta()
