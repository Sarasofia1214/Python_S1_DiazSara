from modulo import funcionprecios
import json
def abrirJSON():
    dicFinal={}
    with open('./1.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./1.json",'w') as outFile:
        json.dump(dic,outFile)




inmuebles={}
booleanito = True
while(booleanito==True):
    print("Bienvenido a la inmobiliaria")
    print("Escribe el nùmero de la opciòn que deseas:")
    print("1.Buscar inmuebles")
    print("2.Editar inmuebles")
    print("3.Agregar inmuebles ")
    print("4.Eliminar inmuebles")
    print("5.Mostrar lista de inmuebles")
    print("6.Salir del programa de la inmobiliaria")
    opcionUsuario= int(input(":"))

    if(opcionUsuario==2):
        funcionprecios()   

    elif(opcionUsuario==3):
        inmuebleNuevo={}
        zonaNuevo=input("Zona A/B:")
        inmuebleNuevo["zona"]=zonaNuevo
        anoNuevo=int(input("Año Construcción:"))
        inmuebleNuevo["año"]=anoNuevo
        metrosNuevo=int(input("Metros Construidos:"))
        inmuebleNuevo["metros"]=metrosNuevo
        habitacionesNuevo=int(input("Habitaciones:"))
        inmuebleNuevo["habitaciones"]=habitacionesNuevo
        garajeNuevo=int(input("¿Tiene garaje?(Si=1,No=0):"))
        if(garajeNuevo==1):
            garaje=1
            inmuebleNuevo["garaje"]=True
        else:
            garaje=0
            inmuebleNuevo["garaje"]=False
        if(inmuebleNuevo["zona"]=="A"):
    
            precioFinalA=((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * ((inmuebleNuevo["año"])/100)
            inmuebleNuevo["precio"]=precioFinalA
        else:

            precioFinalB=((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * ((inmuebleNuevo["año"])/100)*1.5
            inmuebleNuevo["precio"]=precioFinalB
        print("Inmueble Nuevo")
        print("Zona:",inmuebleNuevo["zona"])
        print("Año de construcción:",inmuebleNuevo["año"])
        print("Tamaño:",inmuebleNuevo["metros"],"m2")
        print("Habitaciones:",inmuebleNuevo["habitaciones"])
        if(inmuebleNuevo["garaje"]==True):
            garaje=1
            print("Garaje: Disponible")
        else:
            garaje=0
            print("Garaje: No disponible")
        print("Precio:",inmuebleNuevo["precio"])
        inmuebles["inmuebles"].append(inmuebleNuevo)
        guardarJSON(inmuebles)








Modulo.py

import json
def abrirJSON():
    dicFinal={}
    with open('./1.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./1.json",'w') as outFile:
        json.dump(dic,outFile)

def funcionprecios():
    inmuebles={}
    inmuebles=abrirJSON()
    print("lista antes")

    for i in range(len(inmuebles["inmuebles"])):
        print("Vivienda", i+1)
        print("zona",inmuebles["inmuebles"][i]["zona"])
        print("Año de construcciòn",inmuebles["inmuebles"][i]["zona"])
        print("tamaño",inmuebles ["inmuebles"][i]["metros"] )
        print("habitaciones:", inmuebles ["inmuebles"][i]["habitaciones"])
        if(inmuebles["inmuebles"][i]["garaje"]==True):
            garaje=1
            print("garaje: disponible")
        else:
            garaje=0
            print("garaje: no dsponible")
        if (inmuebles["inmuebles"][i]["zona"]=="A"):
            prefA=((inmuebles["inmuebles"][i]["metros"])*1000 + (inmuebles["inmuebles"][i]["habitaciones"]*5000 + ((inmuebles["inmuebles"][i]["garaje"]*15000)(inmuebles["inmuebles"][i]["año"]/100))))
            inmuebles["inmuebles"][i]["precio"]=prefA
        elif (inmuebles["inmuebles"][i]["zona"]=="B"):
            prefB=((inmuebles["inmuebles"][i]["metros"])*1000 + (inmuebles["inmuebles"][i]["habitaciones"]*5000 + ((inmuebles["inmuebles"][i]["garaje"]*15000)(inmuebles["inmuebles"][i]["año"]/100)))*1.5)
            inmuebles["inmuebles"][i]["precio"]=prefB

    print("Inmuebles ahora")
    for i in range(len[inmuebles]):
        print("Vivienda",i+1)
        print("zona:",inmuebles["inmuebles"][i]["zona"])
        print("año:",inmuebles["inmuebles"][i]["año"])
        print("año:",inmuebles["inmuebles"][i]["metros"])
        print("año:",inmuebles["inmuebles"][i]["habitaciones"])
        if(inmuebles["inmuebles"][i]["garaje"]==True):
            garaje=1
            print("garaje: disponible")
        else:
            garaje=0
            print("garaje: no dsponible")

    print("Precio:",inmuebles["inmuebles"][i]["precio"])
    guardarJSON(inmuebles)
    return inmuebles
