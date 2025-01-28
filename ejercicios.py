def crear_lista():
    l = []
    longitud = int(input("Digite la longitud de su lista: "))
    while longitud <= 2:
        print("La longitud de un palíndrome no puede ser menor a dos elementos")
        longitud = int(input("Digite la longitud de su lista: "))
    for i in range(longitud):
        elementos = input(f"Digite su elemento número {i + 1}: ")
        l1 = l.append(elementos)
    return l 

print("-----------------------Programa que evalúa si la lista es o no palíndrome-----------------------")
lista_1 = crear_lista()
n = len(lista_1)
es_palindrome = True
for i in range (n): #Se generarán números de 0 hasta el valor de la longitud de la lista
    if lista_1[i] != lista_1[(len(lista_1) - 1 - i)]: #Se recurre al elemento en la posición indicada por el número i, si este es igual al elemento indicado en la posición n-1-i, es verdadero
        es_palindrome = False
        break
if es_palindrome:
    print("Su lista es palíndrome")
elif n <= 2:
    print("Un palíndrome debe tener más de dos elementos")
else:
    print(f"Su lista {lista_1} no es palíndrome")
