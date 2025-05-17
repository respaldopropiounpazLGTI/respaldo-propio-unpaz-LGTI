#Hacer un programa en el que se ingresa precio y calcula el precio final con el iva
#(21%). Mostrar el resultado por pantalla
def iva(a):
	precio= a*0.21
	return a+precio

def menu():
	precio=int(input(" ingrese precio "))
	print(" el precio es ",iva(precio))
	
	
menu()