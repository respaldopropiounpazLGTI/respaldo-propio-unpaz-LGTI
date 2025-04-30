#30. Escribir un programa que solicite la fecha de nacimiento en formato “dd/mm/aaaa”, y
# muestre por pantalla la fecha por separado el día,el mes y el año. Ejemplo: El usuario
# ingresa “23/08/2022” el programa debe mostrar:
# “ Día:23 - Mes:08 - Año:2022 ”.
fechas=input(" ingrese fecha de nacimiento en formato dd/mm/aaaa  ")
print(fechas)
print("dia:",fechas[:2],"mes:",fechas[3:5],"año:",fechas[6:]) ,
