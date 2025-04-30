#23. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión.
invertir=int(input(" ingrese cantidad a invertir "))
interes=float(input(" ingrese  el interes anual "))
anios=int(input(" ingrese la cantidad de años a invertir "))
capital=((interes*interes)*anios)
print("invirtio ",invertir,"mas la suma de intereses + los años da como resultado ",capital)