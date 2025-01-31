##//Ejercicio1_DiazSara
def  celsius (temperature1):
    temperature2=(temperature1-32)*(5/9)
    return temperature2
def fahrenheit(temperature2):
    temperature1=(temperature2-32)*(5/9)
    return temperature1
n=float(input("Ingrese la temperatura: "))
option=int(input("Ingresa 1 para calcular celsius a fahrenheit o 2 para calcular fahrenheit a celsius: "))
if option==1:
    print("La temperatura en fahrenheit es: ", (celsius (n)))
else:
    if option==2:
        print("La temperatura en celsius:",(fahrenheit(n)))
    elif option!=1 and option !=2:
        print("El numero ingresado es invalido")
## Sara Dìaz - T.I 1099741170