#Escribir un programa que solicite la fecha de nacimiento en formato
#“dd/mm/aaaa”, y muestre por pantalla la fecha por separado
#el día, el mes y el año. Ejemplo: El usuario ingresa “30/08/2025”
#el programa debe mostrar: “Día: 30 - Mes: 08 – Año:2025”.


def fecha():
	fecha_de_nacimiento=input(" ingrese fecha de nacimiento en formato  **/**/**** ")
	return fecha_de_nacimiento




def muestro():
	opcion_recibida=fecha()
	print("DIA:",opcion_recibida[:2],"MES:",opcion_recibida[4:5],"AÑO:",opcion_recibida[6:])



muestro()