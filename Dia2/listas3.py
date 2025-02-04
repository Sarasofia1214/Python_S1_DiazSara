##//Ejercicio3_DiazSara
def par_impar(n):
   if n % 2 == 0:
      print("El número es par")
   else:
      print("El número es impar")
      
def primo_compuesto(nu):
   if nu <= 1:
      print("El número no es ni primo ni compuesto")
   elif nu == 2:
      print("El número es primo")
   else:
      for i in range(2, int(nu**0.5) + 1): 
         if nu % i == 0:
            print("Es un número compuesto")
            return
      print("Es un número primo")

def cuadrado_perfecto(num):
   cu = int(num**0.5)
   if cu * cu == num:
      print("Es un cuadrado perfecto")
   else:
      print("No es un cuadrado perfecto")

x = int(input("Ingrese un número:"))
par_impar(x)
primo_compuesto(x)
cuadrado_perfecto(x)
 ## Sara Dìaz - T.I 1099741170