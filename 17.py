#17. Escribir un programa que muestre por pantalla, el resultado de 27 dividido 5 y el resto
#de esa división (recuerde cómo se calcula el resto, busque el operador de Python en la
#guía de estudio), almacene cada valor en una variable distinta.
division=27/5
print(division)
resto= 27%5
#el resto es util para saber cuando un numero es par o inpar seria numero %2==0 sria par si no inpar ** no olvidar!!
print(resto)
if resto %2 ==0:
	print("par")
else:
	print("inpar")