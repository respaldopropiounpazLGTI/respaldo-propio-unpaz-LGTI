#24. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
# hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así
# que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a
# demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea
# el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
# del paquete que será enviado
ventas=int(input("que vendio usted hoy ? oprima  1 para payasos o oprima  2 para muñecas,gracias "))
if ventas==1:
	venta_payasos=int(input(" ingrese cantidad (payasos) : "))
	peso_payaso=112
	total_peso_para_payasos=peso_payaso*venta_payasos
	print("total peso para payasos es de :", total_peso_para_payasos,"g")
if ventas==2:
		venta_munecas=int(input(" ingrese la cantidad de ventas para muñecas : "))
		peso_muneca=75
		peso_total_munecas=peso_muneca*venta_munecas
		print("total peso muñecas es de :",peso_total_munecas,"g")

