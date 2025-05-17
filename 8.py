#Hacer un programa en el que ingresas un número que representa cierta cantidad de
#una fruta y divides esa cantidad por 3 chicos. Mostrar por pantalla el resultado
def reparto(a):
	return a/3

def menu():
	fruta=int(input(" ingrese cantidad de kilos de fruta "))
	print(f" la cantidad por cada chico es ",reparto(fruta))
	
	
menu()