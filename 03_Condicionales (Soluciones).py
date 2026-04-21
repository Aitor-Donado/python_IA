# Creamos la lista.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_numeros=list(range(1, 11))

from random import shuffle

shuffle(lista_numeros)


# Comprobar si el tercer elemento es mayor que el septimo.
tercero = lista_numeros[2]
septimo = lista_numeros[6]
if tercero > septimo:
    print (f"El tercer elemento de la lista es mayor que el septimo y es {tercero}")
else:
    print ("El tercer elemento de la lista es menor o igual que el septimo y es " + str(tercero))
    
# Invertir el orden de la lista
lista_numeros.reverse()

# Ordenar por orden inverso (mayor a menor)
# lista_numeros.sort(reverse=True)

# Repetimos la comprobacion
if lista_numeros [2] > lista_numeros [6]:
    print("El tercer elemento de la lista es mayor que el septimo y es " + str(lista_numeros[2]))
else:
    print("El tercer elemento de la lista es menor que el septimo y es " + str(lista_numeros[2]))


# Añadimos la posibilidad de que sea igual.
if lista_numeros [2] > lista_numeros [6]:
    print ("El tercer elemento de la lista es mayor que el septimo y es " + str(lista_numeros[2]))
elif lista_numeros [2] == lista_numeros [6]:
    print ("El tercer elemento de la lista es igual que el septimo y es " + str(lista_numeros[2]))
else:
    print ("El tercer elemento de la lista es menor que el septimo y es " + str(lista_numeros[2])) 
    

# Transformamos el septimo elemento
lista_numeros[6]= lista_numeros[2]


# Comprobamos
if lista_numeros[2] > lista_numeros[6]:
    print ("El tercer elemento de la lista es mayor que el septimo y es " + str(lista_numeros[2]))
elif lista_numeros[2] == lista_numeros[6]:
    print ("El tercer elemento de la lista es igual que el septimo y es " + str(lista_numeros[2]))
else:
    print ("El tercer elemento de la lista es menor que el septimo y es " + str(lista_numeros[2]))   
