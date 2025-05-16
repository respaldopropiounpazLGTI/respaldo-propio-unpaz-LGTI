# 7. Escriba un programa que permita ingresar dos números enteros positivos.
# • Muestre por pantalla el menor, si son iguales muestre un notificando que son iguales y que vuelva a pedirlos.
# • Muestre por pantalla el resultado de la multiplicación entre los números ingresados.

def mutiplicacion(a,b):
	return a*b



def mi_menu():
	while True:
		numero1=int(input(" ingrese primer  numero "))
		numero2=int(input(" ingrese segundo numero "))
		if numero1 <0 or numero2<0:
			print(" solo ambos numeros positivos ")
		if  numero1==numero2:
			print(" numeros iguales vuelva a cargarlos ! ")
		if numero1>numero2:
			print("numero ",numero1,"es mayor")
			print("la mutiplicacion es ",mutiplicacion(numero1,numero2))
		elif numero1<numero2:
			print(" numero ",numero2,"es mayor ")
			print("la multiplicacion es ",mutiplicacion(numero1,numero2))
			
				

	
	
		
		
mi_menu()