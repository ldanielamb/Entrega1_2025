"""Programa que determine si una lista es palíndrome, 
una lista es palíndrome si el elemento en la posición i es el 
mismo de la posición n - 1 - i con n la longitud de la lista"""
lista_1 = ["hola", "si", "si", "hola"] #Creación de una lista palíndrome
for i in range (len(lista_1)): #Se generarán números de 0 hasta el valor de la longitud de la lista
    if lista_1[i] == lista_1[(len(lista_1) - 1 - i)]: #Se recurre al elemento en la posición indicada por el número i, si este es igual al elemento indicado en la posición n-1-i, es verdadero
        print("Su lista es palíndrome") #Ej: i = a 0, luego, se evalúa la posición 0 de la lista. Si el elemento es igual al de la posición (4 - 1 - 0), es palíndrome
    else: 
        print("Su lista no es palíndrome")
print(len(lista_1))
