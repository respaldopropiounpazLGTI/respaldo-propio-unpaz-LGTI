#40 Escriba un programa que pida dos números y que muestre cuál es el menor y cuál el
# mayor o que muestre si son iguales.
numero1=int(input(" ingrese primer numero "))
numero2=int(input(" ingrese segundo valor "))
if numero1>numero2:
	print(" valor1 nº",numero1,"es superior")
elif numero2>numero1:
	print(" valor2 nº",numero2," es superior ")
elif numero1==numero2:
	print(" ambos valores son iguales ")
else:
	print(" valor fuera de rango ")
