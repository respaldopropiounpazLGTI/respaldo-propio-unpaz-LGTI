#1. Escribir un programa que ayude a escoger un destino para irse de vacaciones,
#entonces, el usuario ingresa por teclado el mes que se tomara las vacaciones (en
#formato numérico), si ingresa el mes diciembre, enero, febrero o marzo,
#mostraremos por pantalla por siguientes puntos turísticos “Mar del plata”, “Santa
#Teresita”, “Córdoba”, “San Luis”, pero si elige los meses junio, julio o agosto
#mostraremos por pantalla "Cataratas", "Bariloche", "Perito Moreno", si elige
#cualquier otro mes mostraremos por pantalla "No tenemos sugerencias cargadas.",
#los sitios turísticos se deben mostrar uno debajo de otro mes.
 #     Por ejemplo: 12 - Mar del Plata Santa Teresita.


def eleccion_mes():
	mes=input("ingrese mes o numero de mes para averiguar destinos para salir oprima el botom  0 :")
	return mes

diciembre= " mar del plata ,santa teresita ,cordoba,san luis "
enero=" mar del plata ,santa teresita ,cordoba,san luis "
febrero=" mar del plata ,santa teresita ,cordoba,san luis "
marzo=" mar del plata ,santa teresita ,cordoba,san luis "
junio="cataratas ,bariloche , perito moreno "
julio=  "cataratas ,bariloche , perito moreno "
agosto=     "cataratas ,bariloche , perito moreno "





def meseseleccion():
	while True:
		opcion_recibida=eleccion_mes()
		if opcion_recibida=="12" or opcion_recibida=="diciembre":
			print(diciembre)
		elif opcion_recibida=="1" or opcion_recibida=="enero":
			print(enero)
		elif opcion_recibida=="2" or opcion_recibida=="febrero":
			print(febrero)
		elif opcion_recibida=="3"or opcion_recibida=="marzo":
			print(marzo)
		elif opcion_recibida=="6" or opcion_recibida=="junio":
			print(junio)
		elif opcion_recibida=="7"or opcion_recibida=="julio":
			print(julio)
		elif opcion_recibida=="8"or opcion_recibida=="agosto":
			print(agosto)
		elif opcion_recibida=="0"or opcion_recibida==0:
			print(" gracias por utilzar el programa ")
			break
		else:print(" no tenemos sugerencias cargadas")



meseseleccion()