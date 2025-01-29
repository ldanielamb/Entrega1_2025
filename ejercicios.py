def crear_lista4():
    l = []
    longitud = int(input("Digite la longitud de su lista: "))
    while longitud <= 2:
        print("La longitud de un palíndrome no puede ser menor a dos elementos")
        longitud = int(input("Digite la longitud de su lista: "))
    for i in range(longitud):
        elementos = input(f"Digite su elemento número {i + 1}: ")
        l1 = l.append(elementos)
    return l
def crear_lista3():
    l = []
    longitud = int(input("Digite la longitud de su lista: "))
    for i in range(longitud):
        elementos = input(f"Digite su elemento número {i + 1}: ")
        l.append(elementos)
    return l
def contiene_dos_o_mas_vocales(cadena):
    vocales = "AEIOUaeiou"
    contador = sum(1 for letra in cadena if letra in vocales)
    return contador >= 2


print("-----------------Programa que evalúa si un elemento es cadena palíndrome-----------------")
lista_2 = crear_lista3()
encontrado_palindromo = False
for cadena in lista_2:
    if cadena == cadena[::-1]:
        print(f"'{cadena}' es un palíndromo")
        encontrado_palindromo = True
if not encontrado_palindromo:
    print("No existe")


print("-----------------------Programa que evalúa dos o más vocales-----------------------")
lista_3 = crear_lista3()
evaluar = [cadena for cadena in lista_3 if contiene_dos_o_mas_vocales(cadena)]
if evaluar:
    for cadena in evaluar:
        print(cadena)
else: 
    print("No existe")


print("-----------------------Programa que evalúa si la lista es o no palíndrome-----------------------")
lista_4 = crear_lista4()
n = len(lista_4)
es_palindrome = True
for i in range (n): #Se generarán números de 0 hasta el valor de la longitud de la lista
    if lista_4[i] != lista_4[(len(lista_4) - 1 - i)]: #Se recurre al elemento en la posición indicada por el número i, si este es igual al elemento indicado en la posición n-1-i, es verdadero
        es_palindrome = False
        break
if es_palindrome:
    print("Su lista es palíndrome")
elif n <= 2:
    print("Un palíndrome debe tener más de dos elementos")
else:
    print(f"Su lista {lista_4} no es palíndrome")
