def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def producto(a,b):
    return a*b

def division(a,b):
    return a/b

#Determina si es un numero primo
def numero_primo(a):
    cont = 0
    for i in range(1,a+1):
        mod = a % i
        if mod == 0:
            cont= cont + 1
    if cont == 2:
         print(a,"Es primo")
    else:
        print(a,"No es primo")



