"""
Código que resuelve la evaluación de módulo 3.
Se solicita que, dada una lista de nombres y algunas de sus ocupaciones, poder separarlos en tres grupos: magos, científicos y otros; y quescribir una función llamdada "hacer_grandioso" que modifique la lista de magos añadiendo la frase "El gran" antes del nombre de cada mago.
También una función llamada "imprimir_nombres" que imprime el nombre de cada persona de la lista.
Finalmente, imprimir la lista antes de ser modificada , luego los magos grandiosos, científicos y finalmente los otros. 
"""

def hacer_grandioso(personajes):
    #Función que recibe una lista de personajes y modifica los nombres de los magos añadiendo "El gran" antes de su nombre.
    for personaje in personajes:
        if personaje in magos:
            index_nombre = personajes.index(personaje)
            personajes[index_nombre] = "El gran " + personaje
            index_rol = magos.index(personaje)
            magos[index_rol] = "El gran " + personaje
            


def imprimir_nombres(personajes, group = ""):
    #Función que recibe una lista de personajes y un grupo (magos, científicos, otros) y muestra los nombres de los personajes de ese grupo.
    if group.lower() == "magos":
        print("*"*20)
        print("Magos Grandiosos: ")
        for personaje in personajes:
            if personaje in magos:
                print(personaje)
        print("*"*20)
        return
    if group.lower() == "cientificos":
        print("*"*20)
        print("Científicos: ")
        for personaje in personajes:
            if personaje in científicos:
                print(personaje)
        print("*"*20)
        return

    if group.lower() == "otros":
        print("*"*20)
        print("Otros: ")
        for personaje in personajes:
            if personaje not in magos and personaje not in científicos:
                print(personaje)
        print("*"*20)
        return
    print("*"*20)
    print("Todos los personajes: ")
    for personaje in personajes:
        print(personaje)
    print("*"*20)
    return

#Lista de personajes
personajes = [
    "Harry Houdini",
    "Newton",
    "David Blaine", 
    "Hawking",
    "Messi", 
    "Teller", 
    "Einstein", 
    "Pele",
    "Juanes"
]
#Listas de magos y científicos
magos = ["Harry Houdini", "David Blaine", "Teller"]
científicos = ["Newton", "Hawking", "Einstein"]

#Funciones
imprimir_nombres(personajes)
hacer_grandioso(personajes)
imprimir_nombres(personajes, "magos")
imprimir_nombres(personajes, "cientificos")
imprimir_nombres(personajes, "otros")
