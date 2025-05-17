#Ingresar dos números e informar la suma, multiplicación, división y resta de ellos. Si
#el segundo número es cero la división debe mostrar “No puede realizarse la
#operación”
def suma(a,b):
	return a+b
def multiplicacion(a,b):
	return a*b
def division(a,b):
	return a/b
def resto(a,b):
	return a%b




def cargo_numeros():
	numero1=int(input(" ingrese primer  valor "))
	numero2=int(input(" ingrese segundo valor"))
	if numero2==0:
		print(" no se puede realizar la operacion")
	else:
		print("la suma es: ",suma(numero1,numero2))
		print("la multiplicacion es: ",multiplicacion(numero1,numero2))
		print("la division es: ",division(numero1,numero2))
		print("el resto es: ",resto(numero1,numero2))

cargo_numeros()