import json
def abrirJSON():
    dicFinal={}
    with open('./bbdd_Fut.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd_Fut.json",'w') as outFile:
        json.dump(dic,outFile)
    
equiposFut={}
booleano=True
while(booleano==True):
    print("Bienvenido a la inmobiliaria")
    print("Escribe el nùmero de la opciòn que deseas:")
    print("1.Editar inmuebles")
    print("2.Agregar inmuebles ")
    print("3.Eliminar inmuebles")
    print("4.Mostrar lista de inmuebles")
    print("5.Salir del programa de la inmobiliaria")
    opcionUsuario= int(input(":"))