def crear_lista(longitud_minima=0):
    l = []
    longitud = int(input("Digite la longitud de su lista: "))
    while longitud <= longitud_minima:
        print(f"La longitud de la lista debe ser mayor que {longitud_minima} elementos")
        longitud = int(input("Digite la longitud de su lista: "))
    for i in range(longitud):
        elementos = input(f"Digite su elemento número {i + 1}: ")
        l.append(elementos)
    return l

def contiene_dos_o_mas_vocales(cadena):
    vocales = "AEIOUaeiou"
    contador = sum(1 for letra in cadena if letra in vocales)
    return contador >= 2

def es_palindrome(cadena):
    return cadena == cadena[::-1]

# 1. Programa que evalúa si en una lista existen elementos repetidos
print("------------------Programa que evalúa si en una lista existen elementos repetidos------------------")
lista_1 = crear_lista(longitud_minima=1)
if len(lista_1) != len(set(lista_1)):
    print("La lista tiene elementos repetidos")
else:
    print("La lista no tiene elementos repetidos")

# 2. Programa que evalúa si un elemento es cadena palíndromo
print("-----------------Programa que evalúa si un elemento es palíndrome-----------------")
lista_2 = crear_lista(longitud_minima=1)
evaluando = False
for cadena in lista_2:
    if es_palindrome(cadena):
        print(f"'{cadena}' es un palíndromo")
        evaluando = True
if not evaluando:
    print("No existe")

# 3. Programa que evalúa dos o más vocales
print("-----------------------Programa que evalúa dos o más vocales-----------------------")
lista_3 = crear_lista(longitud_minima=1)
evaluar = [cadena for cadena in lista_3 if contiene_dos_o_mas_vocales(cadena)]
if evaluar:
    for cadena in evaluar:
        print(cadena)
else: 
    print("No existe")

# 4. Programa que evalúa si la lista es o no palíndromo
print("-----------------------Programa que evalúa si la lista es o no palíndromo-----------------------")
lista_4 = crear_lista(longitud_minima=2)
if es_palindrome(lista_4):
    print("Su lista es palíndromo")
else:
    print(f"Su lista {lista_4} no es palíndromo")


