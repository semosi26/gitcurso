# and, or , not

# and ambos valores tienes que ser "true"
# or uno de los valores tienes que ser "true"
# not cambia el valor al opuesto
gas = False
encendido = True
edad = 18

#primero se evaluan los parentesis
if not  gas and (encendido or edad>17):
    print("Puedes avanzar")
