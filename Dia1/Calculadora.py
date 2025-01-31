##//Calculadora_DiazSara
num1= int(input("Escribe el número:  "))
num2= int(input("Escribe otro número: "))
operacion=int(input("Escribe el nùmero de la operacion que deseas realizar (1.suma, 2.resta, 3.multiplicacion, 4.division) : "))

if operacion==1:
    suma1 = num1 + num2
    print("La suma es",suma1)
else:
    if operacion==2:
        resta1 = num1 - num2
        print("La resta es",resta1)
    else:
        if operacion==3:
            producto = num1 * num2
            print("La multiplicación es",producto)
        else:
                if operacion==4:
                    division1 = num1 / num2
                    print("La división es",division1)
 ## Sara Dìaz - T.I 1099741170