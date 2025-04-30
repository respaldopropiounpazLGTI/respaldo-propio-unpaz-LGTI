#35. Escribir un programa que permita ingresar su año de nacimiento sin
# decimales, y calcular SI ya pasaron 18 años, si ya pasaron 18 años, mostrar cuantos
# años pasaron desde que cumplio los 18 años junto al mensaje que diga: “Ud es mayor
# de edad hace: ......años, porque este año usted tendrá .... años". Indique la finalización
# del programa
anio=int(input(" ingrese su año de nacimiento "))
print("")
actual=2025
mayor=actual-anio
resta=mayor-18
print("por que este año usted tendra " ,mayor ," años ")
print("")
if mayor>18:
	print("hace ",resta," que paso los 18 años de edad  ")
else:
	print("usted es menor de edad  ")
print("")
print("fin del programa ")

