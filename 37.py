#37. Escribir un programa permita el ingreso de una letra, el programa debe mostrar un
# aviso si la letra es vocal o consonante.
letra=input("ingrese letra : ")
a="letra vocal"
e="letra vocal"
i="letra vocal"
o="letra vocal"
u="letra vocal"
if letra=="a":
	print(a)
elif letra=="e":
	print(e)
elif letra=="i":
	print(i)
elif letra=="o":
	print(o)
elif letra=="u":
	print(u)
else:
	print("letra",letra,"consonante")
