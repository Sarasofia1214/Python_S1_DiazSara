##//Ejercicio1_DiazSara
def ed (a,b,c,d,e):
    b[a-1]=c
    d[a-1]=e

def ana(a,b,c,d):
     c.append(a)
     d.append(b)

def delete (a,b,c):
     b.pop(a-1)  
     c.pop(a-1)

def n (a,b):
    for i in range(len(a)):
            nombret=" ".join(a[i])+" "+" ".join(b[i])
            print (f"{i+1}, {nombret}") 
## Sara Dìaz - T.I 1099741170
