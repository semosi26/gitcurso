def suma(a,b,c):
    print(a+b+c)

suma(2,5,7)  


def suma2(*numeros):
    resultado=0
    for numero in numeros:
        resultado+=numero
    print(resultado)

suma2(2,5,7,45,32)  