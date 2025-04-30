#38. Escribir un programa que ayude a escoger un destino para irse de vacaciones,
# entonces, el usuario ingresa por teclado el mes que se tomara las vacaciones (en
# formato numérico), si ingresa el mes diciembre, enero, febrero o marzo, mostraremos
# por pantalla por siguientes puntos turísticos “Mar del plata”, “Santa Teresita”,
# “Córdoba”, “San Luis”, pero si elige los meses junio, julio o agosto mostraremos por
# pantalla "Cataratas", "Bariloche", "Perito Moreno", si elige cualquier otro mes
# mostraremos por pantalla "No tenemos sugerencias cargadas.", los sitios turísticos se
# deben mostrar uno debajo de otro. mes:
# Por ejemplo:
# 12 - Mar del plata Santa Teresita

print("bienvenido a sus proximas vaciones :)")
print ("ingrese mes o numero de mes para organizar sus vacaciones")
print("")
mes=input("por ejemplo  12 / diciembre para  ==> Mar del plata Santa Teresita :  " )



diciembre = "Santa Teresita,Córdoba,y San Luis "
enero=  "Santa Teresita,Córdoba,y San Luis  "
febrero="Santa Teresita,Córdoba,y San Luis  "
marzo="Santa Teresita,Córdoba,y San Luis "
junio="Cataratas", "Bariloche", "Perito Moreno"
julio="Cataratas", "Bariloche", "Perito Moreno"
agosto="Cataratas", "Bariloche", "Perito Moreno"

if mes=="diciembre":
	print(diciembre)
elif mes=="12":
	print(diciembre)
elif mes=="enero":
	print(enero)
elif mes=="1":
	print(enero)
elif mes=="febrero":
	print(febrero)
elif mes=="2":
	print(febrero)
elif mes=="marzo":
	print(marzo)
elif mes=="3":
	print(marzo)
elif mes=="junio":
	print(junio)
elif mes=="6":
	print(junio)
elif mes=="julio":
	print(julio)
elif mes=="7":
	print(julio)
elif mes=="agosto":
	print(agosto)
elif mes=="8":
	print(agosto)
else:
	print( "No tenemos sugerencias cargadas." )






