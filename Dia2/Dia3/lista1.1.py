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

print("Estudiante#",": ",nombres)

print("\n##############")
print("\n##############")

print("Estudiante#",": ",apellidos)

print("\n##############")
print("\n##############")




    
for i in range(len(nombres)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",nombres[i])
numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
nombres[numeroEstudiante-1]=nombreEstudianteNuevo



for i in range(len(apellidos)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",apellidos[i])
numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
apellidoEstudianteNuevo=input("Cual será el apellido nuevo del estudiante?:")
apellidos[numeroEstudiante-1]=apellidoEstudianteNuevo
print("Estudiante#",i+1,": ",apellidos[i])