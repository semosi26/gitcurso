def largo(texto):
    resultado=0
    for _ in texto:
        resultado+=1
    return(resultado)
    
print("chanchito") #punto rojo (breakpoint)
#el depurador se detendra en esta linea antes de seguir avanzando
l=largo("Hola Mundo")
print(l)

#La depuracion es como ver como se manejan las funciones por dentro
#para si poder ver donde podria estar nuestro error

