#Hacer un algoritmo que ingrese dos números y determinar si alguno de los dos
#números es divisible por 3.

def pedir_numero():
	numero1=int(input(" ingrese numero 1 "))
	numero2=int(input(" ingrese numero 2 "))
	if numero1%3==0 or numero2%3==0:
		print(" algun de los dos es divisible ")
	else:print(" no hay valor divisible ")
	
	
pedir_numero()

