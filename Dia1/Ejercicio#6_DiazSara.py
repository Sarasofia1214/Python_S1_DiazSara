##//Ejercicio7_DiazSara
n=0
totalbruto=0
totaleps=0
totalpension=0
totalneto=0 
bruto=0
mayorsueldo=0
menorsueldo=0
nombremenor=0
promediobruto=0
n=int(input("Ingresa el numero de empleados: "))
for i in range (n) :
    
    nombre=input("Ingresa el nombre del empleado: ")
    horas=int(input("Ingresa las horas trabjadas del empleado:"))
    bruto=horas*20000
    eps=bruto*0.04
    pension=bruto*0.04
    neto=bruto-eps-pension
    

    print("Empledo: ",nombre)
    print("")
    print("Sueldo bruto: ",bruto)
    print("")
    print("EPS: ",eps)
    print("")
    print("Pensión: ",pension)
    print("")
    print("Sueldo neto: ",neto)

    if neto > mayorsueldo:
        menorsueldo=mayorsueldo
        mayorsueldo=neto 
        nombremayor=nombre
    else:
        if mayorsueldo > menorsueldo:
            menorsueldo=neto
            nombremenor=nombre


totalbruto=totalbruto+bruto
totaleps=totaleps+eps
totalpension=totalpension+pension
totalneto=totalneto+neto
    


    
print("Datos totales:")
print("")

promediobruto=totalbruto/n
promedioneto=totalneto/n
print("Total salario bruto: ",totalbruto)
print("")
print("Total EPS: ",totaleps)
print("")
print("Total pensión: ",totalpension)
print("")
print("Total sueldo neto: ",totalneto)
print("")
print("Empleado con mayor sueldo neto:",nombremayor)
print("")
print("Sueldo de empleado con mayor sueldo: ",mayorsueldo)
print("")
print("Empleado con menor sueldo neto:",nombremenor)
print("")
print("Sueldo de empleado con menor sueldo: ",menorsueldo)
print("")
print("Promedio salario neto:",promedioneto)
print("")
print("Promedio salario bruto:",promediobruto)
 ## Sara Dìaz - T.I 1099741170