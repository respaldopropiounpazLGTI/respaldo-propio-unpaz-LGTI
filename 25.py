#25. Una panadería vende una baguette a $50 cada una. La baguette que no es el día tiene
# un descuento del 60%. Escribir un programa que comience leyendo el número de
# baguette vendidas que no son del día. Después el programa debe mostrar el precio
# habitual de una baguette, el descuento que se le hace por no ser fresca y el costo final
# total con descuento.
precio_vaguette=50
venta_del_dia=int(input(" ingrese la cantidad de vaguette vendidas "))
venta_normal=venta_del_dia*precio_vaguette
descuento=venta_normal*0.60
total_pagar=venta_normal-descuento
print("precio normal total vaguetes ",venta_normal)
print("precio normal sin descuento  ",venta_normal, "-", "descuento del 60% ",descuento)
print("se aplica un descuento del 60% por no ser un producto fresco total al pagar ",total_pagar)
#a revisar no se si esta bien !!!! 


