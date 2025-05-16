#    6. Escribir un programa que simule un juego de adivinanza. El programa deberá elegir un número aleatorio entre 1 y 100,
#    y pedirle al usuario que adivine cuál es el número. El usuario deberá ingresar un número,
#    y el programa deberá decirle si el número ingresado es mayor o menor que el número a adivinar.
#    El juego termina cuando el usuario adivina el número correcto, y se le muestra al usuario cuántos
#    intentos le llevó. Nota: Solo tiene 5 intentos.

import random
numero_adivinar=random.randint(1,100)
print(numero_adivinar)

#variasbles ver numero y suma y resta son de apoyo para ver si voy bien!
def pregunta():
	intentos=0
	while True:
	
		numero_usuario=int(input(" ingrese su numero "))
		if numero_usuario==numero_adivinar:
			intentos+=1
			print("felicitaciones usted a adivinado el numero !!! en  ",intentos,"intentos!!!")
		elif numero_usuario>numero_adivinar:
			intentos+=1
			diferencia=numero_usuario-numero_adivinar
			print("se paso el numero por :",diferencia)
		elif numero_usuario<numero_adivinar:
			intentos+=1
			diferenciamas=numero_adivinar-numero_usuario
			print(" su numero es muy bajo le faltam :",diferenciamas)
		elif intentos==5:
			print(" usted se quedo sin intentos !!!! ")
			break
			

pregunta()