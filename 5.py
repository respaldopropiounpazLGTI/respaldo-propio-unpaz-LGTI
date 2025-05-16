#Calculadora: Crea un programa que pida al usuario que ingrese dos números y luego le pregunte
# qué operación quiere realizar (suma, resta, multiplicación o división).
# El programa debe realizar la operación elegida por el usuario y mostrar el resultado.
# Luego, debe preguntarle al usuario si quiere realizar otra operación, y continuar pidiendo números y
# realizando operaciones hasta que el usuario responda "no".d

def suma(a,b):
	return a+b
def resta(a,b):
	return a-b
def division(a,b):
	return a/b
def multiplicacion(a,b):
	return a*b
def mi_menu():
	while True:
		numero1=int(input(" ingrese primer  numero "))
		numero2=int(input(" ingrese segundo numero "))
		print("suma")
		print("resta")
		print("multiplicacion")
		print("division")
		pregunta=input(" que operacion desea realizar  ").lower()
		if pregunta=="suma":
			print(" la suma es ",suma(numero1,numero2))
		elif pregunta=="resta":
			print(" la resta es ",resta(numero1,numero2))
		elif pregunta=="division":
			print("la division es ",division(numero1,numero2))
		elif pregunta=="multiplicacion":
			print("la multiplicacion es ",multiplicacion(numero1,numero2))
		else:print(" opcion incorrecta")
		sigue=input("desea realizar otra operacion? ")
		if sigue==("no").lower():
			break
	
mi_menu()