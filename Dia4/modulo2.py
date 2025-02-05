##//Ejercicio1.1_DiazSara
from modulo1 import *
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
     ["Vladimir"]
]



apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
booleano= True
while (booleano==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Editar nombre del estudiante")
    print("2.Agregar estudiante")
    print("3.Eliminar estudiante")
    print("4.Mostrar lista estudiantes")
    print("5.Salir del programa")
    opcionUsuario= int(input(":"))
  
    if (opcionUsuario==1):
        n (nombres, apellidos)
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudiante=input("Cual será el nuevo nombre del estudiante?:")
        apellidoEstudiante=input("Cual será el nuevo apellido del estudiante?:")
        
        ed(numeroEstudiante, nombres, nombreEstudiante, apellidos, apellidoEstudiante)
        
    elif (opcionUsuario==2):
        n (nombres, apellidos)
        nombreN=input("Cual será el nombre nuevo del estudiante?:")
        apellidoN=input("Cual será el apellido nuevo del estudiante?:")
        ana(nombreN, apellidoN, nombres, apellidos)

    elif(opcionUsuario==3):
        n (nombres, apellidos)
        numeroEstudiante=int(input("Cual numero de estudiante quieres eliminar?:"))
        delete (numeroEstudiante, nombres, apellidos)

    elif opcionUsuario==4:
        n (nombres, apellidos)

    elif opcionUsuario==5:
        booleano= False
        break
## Sara Dìaz - T.I 1099741170
    
