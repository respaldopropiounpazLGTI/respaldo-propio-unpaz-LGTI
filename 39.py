#39.Escribir un programa que permita calcular la suma de tres números enteros ingresados
# por teclado.
# Si el resultado es mayor a 50 dividir por 2
# En caso contrario elevar el resultado al cubo,
# si al calcular el cubo el resultado es superior a 5000 deberá mostrar
# por pantalla “Este es un gran número”
numero1=int(input(" imgrese primero numero a sumar "))
numero2=int(input(" ingrese segundo numero a sumar "))
numero3=int(input(" ingrese tercer numero a sumar "))
suma =numero1+numero2+numero3
division=(suma/2)
cubo= (suma**3)
superior=5000
mensaje="este es un gran numero "
if suma>50:
	print("la suma es :",suma,  "como la suma supera los 50 se procede con la division es ",division)
elif print("la suma es ",suma," no supera los 50 se procede con elevar al cubo  ",cubo):
	if cubo>superior:
		print(" este es un gran numero ")
	else:
		print(" valor final ",cubo)
#no estoy seguro si esta bien la logica queda pendiente consultar con el profesor 
