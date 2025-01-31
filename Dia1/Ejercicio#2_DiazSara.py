##//Ejercicio2_DiazSara
cantidadterminos=int (input("La cantidad de terminos son: "))
sumatoria=0
for i in range (1,cantidadterminos +1):
        if i%2==0:
           sumatoria=sumatoria-(1/i)
        else:
            sumatoria=sumatoria+(1/i)

(print("La sumatoria es: ", sumatoria))
 ## Sara Dìaz - T.I 1099741170
