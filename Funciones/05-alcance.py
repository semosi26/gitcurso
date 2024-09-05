
saludo="Hola GLobal"

def saludar():
    global saludo # es la que esta afuera 
    saludo="hola mundo"
    print(saludo)

def saluda_chanchito():
    saludo="Hola Chanchito"
    print(saludo)


saludar()


# NO UTILIZAR VARIBALES GLOBALES 
# MALAS PRACTICAS