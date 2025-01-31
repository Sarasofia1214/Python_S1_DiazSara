##//Ejercicio7_DiazSara
num1=int(input("ingrese el primer número: "))
num2=int(input("ingrese el segundo número: "))
SUMA1=0
SUMA2=0
for i in range (1,num1) :
    if num1 % i == 0:
        SUMA1=SUMA1+i
for i in range (1,num2):
    if num2 % i ==0:
        SUMA2=SUMA2+i

if SUMA1==num2 and SUMA2==num1 :
    print( "Son numeros amigos")
else:
    print("No son numeros amigos")
## Sara Dìaz - T.I 1099741170