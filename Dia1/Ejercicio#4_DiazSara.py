##//Ejercicio4_DiazSara
grande=0
pequeno=0
for i in range (1,11):   
    num=int(input("Ingresa el numero: "))   
    if i==1:
      grande=num
      pequeno=num
    elif num > grande:
       grande=num
    elif num < pequeno:
       pequeno=num
print("El numero mayor es: ",grande)
print("El numero menor: ",pequeno)
 ## Sara Dìaz - T.I 1099741170