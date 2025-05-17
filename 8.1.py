#Hacer un programa que ingresa un precio y calcula un descuento del 9%. Mostrar
#por pantalla el resultado

def descuento(a):
	precio_comun=a*0.09
	descuento=a-precio_comun
	return descuento



def menu():
	numero1=int(input(" ingrese precio"))
	print(" el descuento es ",descuento(numero1))
	
	
	
menu()
