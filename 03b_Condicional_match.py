# La sentencia `match` se utiliza para realizar diferentes acciones basadas en diferentes condiciones.

## La Sentencia Match en Python
'''
En lugar de escribir muchas sentencias `if..else`, puedes usar la sentencia `match`.

La sentencia `match` selecciona uno de muchos bloques de código para ser ejecutado.
'''
### Sintaxis
'''
Así es como funciona:

1. La expresión `match` se evalúa una vez.
2. El valor de la expresión se compara con los valores de cada caso.
3. Si hay coincidencia, se ejecuta el bloque de código asociado.

El siguiente ejemplo usa el número del día de la semana para imprimir el nombre del día:
'''
### Ejemplo

día = 4
match día:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")


## Valor por Defecto
'''
Usa el carácter guión bajo `_` como último valor de caso si quieres que un bloque de código se ejecute cuando no hay otras coincidencias:
'''
### Ejemplo


día = 4
match día:
    case 6:
        print("Hoy es Sábado")
    case 7:
        print("Hoy es Domingo")
    case _:
        print("Esperando el fin de semana")

'''
El valor `_` siempre coincidirá, por lo que es importante colocarlo como último caso para que funcione como caso por defecto.
'''
## Combinar Valores
'''
Usa el carácter barra vertical `|` como operador "o" en la evaluación del caso para verificar más de un valor coincidente en un solo caso:
'''
### Ejemplo


día = 4
match día:
    case 1 | 2 | 3 | 4 | 5:
        print("Hoy es día laboral")
    case 6 | 7:
        print("¡Me encantan los fines de semana!")


## Sentencias If como Guardias
'''
Puedes agregar sentencias `if` en la evaluación del caso como una condición adicional:
'''
### Ejemplo


mes = 5
día = 3
match día:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Un día laboral en Abril")
    case 1 | 2 | 3 | 4 | 5 if mes == 5:
        print("Un día laboral en Mayo")
    case _:
        print("Sin coincidencia")
