#Hacer un algoritmo que nos permita introducir un número, luego muestre por
#pantalla el mensaje “Este número es positivo” o “Este número es negativo”

def pedir_numero():
	numero=int(input(" ingrese numero "))
	if numero>0:
		print(" es positivos ")
	else:
		print(" es negativo")
		
		
		
		
pedir_numero()