# #
# Desafío a Entregar: Ahorcado
# Los desafíos se entregan mediante esta página de HackerRank. Pueden ver un instructivo acerca del uso de la plataforma en este link.

# Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y otro jugador intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree que se encuentra en la palabra elegida.

# Una vez que el segundo jugador adivina todas las letras que se encuentran en la palabra, el juego termina y se muestra la cantidad de intentos que fueron necesarios. En esta versión del juego, si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias cuentan como adivinadas.

# Formato del input:

# Primero se recibe la palabra que se debe adivinar (por defecto vendrá en mayúsculas).
# Luego se reciben cierta cantidad de letras, una por línea, sin repetir. (por defecto vendrán en mayúsculas).
# Una vez que se haya adivinado la palabra del ahorcado, ya no se recibirán más letras. Su tarea es determinar la cantidad de intentos que fueron necesarios para adivinar la palabra completa, e imprimir ese número.

# Ejemplos:

# Ejemplo 1

# Input:

# PYTHON
# A
# B
# C
# P
# Y
# T
# H
# O
# N
# Output:

# 9
# El programa imprime la cantidad de turnos que se tardaron en adivinar la palabra, a pesar de que tuvo tres intentos erróneos ('A','B' y 'C')

# Ejemplo 2:

# Input:

# IEEE
# X
# Y
# E
# I
# Output:

# 4
# La palabra original tiene letras repetidas, por lo cual al adivinar las letras 'I' y 'E' alcanza para completar la palabra.


# Tip: Pueden eliminar todas las ocurrencias de cierto carácter en un string utilizando el método .replace():

# palabra = palabra.replace( "A", "" )

# Challenge (No se entrega en la corrección automática):

# Agregar una condición de perder, en el caso de que se haya superado cierta cantidad de intentos.
# Mostrar un contador de letras incorrectas, incrementarlo si la letra no esta en la palabra.
# Mostrar la palabra con guiones bajos _ en donde haya una letra que el jugador todavía no adivinó y mostrar las letras que sí adivinó. Por ejemplo, para la palabra AHORCADO debe mostrar: A _ O _ _ A _ O si el jugador ya ingreso las letras A, O y P.
# Armar una representación de la persona ahorcada del juego usando Arte ASCII, si prefieren pueden usar los dibujos ya creados por otras personas en internet.
