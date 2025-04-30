#21. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# costo por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas=int(input(" ingrese las horas trabajadas  "))
coste=float(input("ingrese el coste por hora  "))
paga=horas*coste
print(paga,"pesos brutos ")