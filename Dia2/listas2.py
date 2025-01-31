##//Ejercicio2_DiazSara
def interes_simple (p,r,t):
    si=(p*r*t)
    return si
def interes_compuesto (p,r,t,n):
    ci= p*(1+r/n)**n*t
    return ci
    
print("Calculadora de interes: ")
p=float(input("Ingresa el valor principal:"))
r=float(input("Ingresa el valor del interes anual en forma decimal:"))
t=float(input("Ingresa el periodo de tiempo: "))

print("El interes simple es: ", interes_simple (p,r,t))
print("Calculadora de interes: ")
p=float(input("Ingresa el valor principal:"))
r=float(input("Ingresa el valor del interes anual en forma decimal:"))
t=float(input("Ingresa el periodo de tiempo: "))
n=float(input("Ingresa el número de veces a aplicar el interés compuesto por año: "))
print("El interes compuesto es:", interes_compuesto (p,r,t,n))
 ## Sara Dìaz - T.I 1099741170