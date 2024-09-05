def suma(a,b):
    resultado=a+b
    print(resultado)

suma(1,2)

def suma2(a,b):
    resultado=a+b
    return resultado

c=suma2(1,2)
d=suma2(c,2)
print(d)