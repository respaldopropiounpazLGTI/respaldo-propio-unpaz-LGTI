#Hacer un algoritmo que pida un número entero y determine si es múltiplo de 5.
#Muestra un mensaje por pantalla.

def pedir_numero():
	numero1=int(input(" ingrese numero "))
	if numero1%5==0:
		print(" es multiplo ")
	else:
		print(" no es multiplo")
		
		
		
pedir_numero()