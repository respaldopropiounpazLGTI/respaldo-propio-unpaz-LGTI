#Escribir un programa que muestre un menú con las siguientes opciones:
#   a. Suma.
#   b. Multiplicación.
#   c. Largo de Palabras.
#    d. Salir.
#Funcionamiento:
#    • El usuario debe ver el menú de opciones todo el tiempo.
#Si elige la opción a: Debe solicitar 2 números, sumarlos y mostrarlos.
#Si elige la opción b: Debe solicitar 2 números, multiplicarlos y mostrarlos.
#Si elige la opción c: Debe solicitar dos palabras y mostrar la palabra más larga,
# avisar cuando sean iguales. En ambos casos debe mostrar el largo de cada una.
#Si elige la opción d: Debe salir y despedir al usuario.

def menu():
		print("a para suma ")
		print("b para multiplicacion")
		print("c largo de palabras")
		print("d para salir ")
		opcion=input(" que desea hacer usted hoy :  ")
		return opcion

def main():
	while True:
		opcion_recibida=menu()
		if opcion_recibida=="suma"or opcion_recibida=="a":
			numero1=int(input(" ingrese valor 1"))
			numero2=int(input(" ingrese valor 2"))
			suma=numero1+numero2
			print(" la suma es ",suma)
		elif opcion_recibida=="b"or opcion_recibida=="multplicacion":
			numero1=int(input(" ingrese primer valor"))
			numero2=int(input(" ingrese segundo valor "))
			multi=numero1*numero2
			print(" la multiplication es ",multi)
		elif opcion_recibida=="c"or opcion_recibida=="largo de palabras":
			parabra1=input("ingrese primer  palabra ")
			parabra2=input("ingrese segundo parabra ")
			if len(parabra1)>len(parabra2):
				print(" palabra 1 es mayor ",parabra1)
			else:print(" palabra 2 es mayor ",parabra2)
		elif opcion_recibida=="d" or opcion_recibida=="salir ":
			print(" gracias por utilizar el programa ")
			break


main()