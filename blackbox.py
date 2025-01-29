print("-------------------contar elementos únicos-------------------")
def contar_elementos_unicos(lista): 
    # Se usa el método set para eliminar de la lista los duplicados que puedan existir
    elementos_unicos = set(lista)
    print(f"Cantidad de elementos únicos: {len(elementos_unicos)}")
    print("Elementos únicos:", elementos_unicos)

# Solicitar la lista al usuario
lista1 = input("Digite los elementos de la lista separados por espacio: ")
# Convertir la entrada en una lista de elementos mediante el método split, que devuelve una lista que contiene las partes de la cadena separadas por un delimitador " ". 
lista = lista1.split()
contar_elementos_unicos(lista)

print("----------------------Encontrar y mostrar la cadena más larga----------------------")
def encontrar_cadena_mas_larga(lista):
    if not lista:
        print("La lista está vacía")
        return

    cadena_mas_larga = lista[0]  # Inicializamos con el primer elemento
    for cadena in lista[1:]:  # Recorremos el resto de la lista
        if len(cadena) > len(cadena_mas_larga):  # Comparamos las longitudes
            cadena_mas_larga = cadena  # Si encontramos una cadena más larga, la actualizamos
    
    print(f"La cadena más larga es: '{cadena_mas_larga}'")

lista2 = input("Digite las cadenas separadas por espacio: ")
lista = lista2.split()
encontrar_cadena_mas_larga(lista)

print("-----------------contar vocales-----------------")
def contar_vocales(cadena):
    # Definir las vocales en minúsculas y mayúsculas
    vocales = "AEIOUaeiou"
    #Se utiliza una list comprehension, cuya sintaxis es [nueva_expresion for item in iterable if condicion]
    #Se recorre cada letra de la cadena con el primer for, se verifica si la letra está en la cadena de vocales con el if, y si es verdadero, se genera un 1
    contador = sum(1 for letra in cadena if letra in vocales)#sum va a sumar todos los 1 que se generan y así obtener el número total de vocales

    return contador

def contar_vocales_en_lista(lista):
    if not lista:  # Verificar si la lista está vacía
        print("La lista está vacía")
    else:
        for cadena in lista:
            numero_vocales = contar_vocales(cadena)
            print(f"'{cadena}' tiene {numero_vocales} vocales")
lista3= input("Digite las cadenas separadas por espacio: ")
lista = lista3.split()
contar_vocales_en_lista(lista)

print("--------------------------contar números primos-----------------------------")
def es_primo(numero):
    if numero < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, numero):  # Recorremos todos los números hasta el número-1
        if numero % i == 0:
            return False  # i es un divisor, por lo tanto, el número no es primo
    return True  # Si no se encontró ningún divisor, es primo

# Función para comprobar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Función para contar los números primos en una lista
def contar_primos(lista):

####primos = [numero for numero in lista if es_primo(numero)]
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    
    # Comprobamos si hay primos en la lista y mostramos el resultado
    if primos:
        print(f"Cantidad de números primos encontrados: {len(primos)}")
    else:
        print("No hay números primos en la lista")

lista4 = input("Digite los números separados por espacio: ")
# Convertir la entrada en una lista de enteros
###lista = [int(x) for x in lista4.split()]
lista = []
for x in lista4.split():
    lista.append(int(x))
contar_primos(lista)



