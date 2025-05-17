#Hacer un algoritmo que nos permita introducir un número, luego muestre por
#pantalla el mensaje “Este número es par” o “este número es impar”

def numero():
	numero1=int(input(" ingrese numero "))
	if numero1%2==0:
		print(" este numero es par ")
	else:
		print(" este numero es inpar")
		
		
		
numero()