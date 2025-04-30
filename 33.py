#33. Escribir un programa que permita el ingreso de 2 digitos, si es menor a 20 debe
# mostrar la mitad de ese número.
digito=int(input(" ingrese solo 2 digitos menores a 20 "))
if digito<20:
	mitad=digito//2
	print(mitad)
else:
	print(" numero no valido solo 2 digito y menores a 20 ")
