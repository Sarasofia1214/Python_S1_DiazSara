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
booleano=True
while(booleano==True):
    print("Bienvenido a la inmobiliaria")
    print("Escribe el nùmero de la opciòn que deseas:")
    print("1.Buscar inmuebles")
    print("2.Editar inmuebles")
    print("3.Agregar inmuebles ")
    print("4.Eliminar inmuebles")
    print("5.Mostrar lista de inmuebles")
    print("6.Salir del programa de la inmobiliaria")
    opcionUsuario= int(input(":"))

    if opcionUsuario==1:
        inmuebles=abrirJSON()
        print(inmuebles["inmuebles"])


        presu=int(input("Escribe tu presupuesto:"))

    elif opcionUsuario==2:
        en=int(input("Cual inmueble quieres editar:"))
        ed=input("Como sera el nuevo imueble:")

        def funcionprecios():
            inmuebles={}
            inmuebles=abrirJSON()
            print("lista antes)")
        
            for i in range(len(inmuebles["inmuebles"])):
                print("Vivienda", i+1)
                print("zona",inmuebles["inmuebles"][i]["zona"])
                print("Año de construcciòn",inmuebles["inmuebles"][i]["zona"])
                print("tamaño",inmuebles ["inmuebles"][i]["metros"] )