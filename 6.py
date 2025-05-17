#Hacer un programa que ingresas la edad de una persona y calcula cuántos años va a
#tener dentro de 23 años. Mostrar el resultado por pantalla.
def mas(a):
	return a+23


def menu():
	edad=int(input(" ingrese edad "))
	print(" destro de 23+ ",mas(edad))
	
	
menu()