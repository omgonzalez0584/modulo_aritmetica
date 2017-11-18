import aritmetica

def main():
    print("Programa que realiza operaciones aritmeticas")
    a = int(input("Introduzca el primer numero: "))
    b = int(input("Introduzca el segundo numero: "))

    c = aritmetica.suma(a,b)
    print("La suma es: ",c)

    c = aritmetica.resta(a,b)
    print("La resta es: ",c)

    c = aritmetica.producto(a,b)
    print("El prodcuto es: ",c)

    c = aritmetica.division(a,b)
    print("La disivion es: ",c)

    d = int(input("Introduza un numero para validar si es primo: "))
    aritmetica.numero_primo(d)

main()

