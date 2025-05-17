#Hacer un programa en el que se ingresa un número entero y por pantalla informa el
# doble de ese número.

def doble(a):
	return a*2


def mi_menu():
	numero1=int(input(" ingrese numero "))
	print(" el dobles ",doble(numero1))
	
	
mi_menu()