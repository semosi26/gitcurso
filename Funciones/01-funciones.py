print("Hola Mundo")
#vamos a crear nuestra propia funcion
def hola():
    print("Hola Mundo")
    print("Ultimate Python")


def hola2(nombre,apellido): #nombre = parametro
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola2("nicolas","more") #"nicolas"=argumento
hola2("Chancito" ,"Feliz")

#ARGUMENTOS OPCIONALES

def hola3(nombre,apellido="Feliz"): #nombre = parametro
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola3("Chancito") #pero el parametro apellido puede cambiar
hola3("Sebas","More")

#ARGUMENTOS NOMBRADOS
def hola4(nombre,apellido="Feliz"): #nombre = parametro
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

hola4(apellido="More",nombre="Sebas")










