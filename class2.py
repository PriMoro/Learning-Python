# Mini-desafío: floats
# Crear:

# Una función que convierta grados Celsius a grados Farenheit. (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
# Una función que convierta grados Celsius a grados Kelvin. (https://es.wikipedia.org/wiki/Kelvin)


# El usuario debe ingresar una temperatura en grados Celsius y el programa debe mostrar las conversiones a Farenheit y Kelvin utilizando las funciones. Si la temperatura ingresada es inferior al cero absoluto, el programa debe mostrar un mensaje de advertencia y pedir que se reingrese la temperatura.

# Pueden leer aquí sobre cómo hacer las conversiones.

# celsius = float(input("Enter your temperature in ° Celsius: "))

# while celsius <= -273.15:
#     celsius = float(
#         input("Error! Enter your temperature in ° Celsius again: "))


# def convertToFarenheit():
#     fahrenheit = celsius * (9 / 5) + 32
#     return fahrenheit


# def convertToKelvin():
#     kelvin = celsius + 273.15
#     return kelvin


# print("Farenheit", convertToFarenheit(),
#       "°F", "Kelvin", convertToKelvin(), "K")

# Mini-desafío: Operaciones con strings
# Hacer un programa que permita ingresar un nombre y un apellido usando dos veces la función input( ).
# Luego debe crear la variable nombre_y_apellido que contenga ambos datos separados por un espacio.
# Un fabricante de tarjetas admite la impresión de hasta 26 caracteres para el nombre del dueño de la tarjeta,
# el programa debe imprimir "Nombre admitido" si nombre_y_apellido cumple con esta restricción y "Nombre no admitido"
# en caso contrario (el espacio cuenta como uno de los 26 caracteres disponibles).


# Para un desafío mayor: Si nombre_y_apellido cumple la restricción, mostrar el nombre y apellido.
# En caso contrario nombre_y_apellido debe valer la inicial del nombre y luego el apellido separado por un espacio.

# Si todavía no se cumple la restricción entonces el valor será la inicial del nombre y las primeras 24 letras del apellido. Mostrar el nombre resultante.4nombre = input("Ingrese el nombre: ")
# Desafío mayor

# name = input("Name: ")
# lastName = input("LastName: ")

# fullName = name + " " + lastName
# if len(fullName) > 26:
#     fullName = name[0] + " " + lastName

#     if len(fullName) > 26:
#         fullName = name[0] + " " + lastName[:24]

# print(fullName)

# Mini-desafío: Listas
# Crear una lista con los números pares menores a 50 ¿Hay diferentes formas de lograr esto?
# evenNumbers = [2 * x for x in range(25)]
# print("Even Numbers Young Than 50: ", evenNumbers)

# Crear un programa en el cual el usuario ingresa un string y dos índices numéricos.
# El programa debe crear una lista a partir de las letras del string,
# luego intercambiar dos letras de lugar a partir de los índices indicados por el usuario.
# Por último debe combinar las letras de la lista nuevamente en un string e imprimir el resultado.
# Si los índices son inválidos mostrar un mensaje de error.

# Tips:

# Usando list( mi_string ) pueden obtener una lista que contiene las letras de mi_string.
# Usando el método str.join() pueden unir las letras o strings de una lista dentro de un mismo string:
# lista = ["Uno", "Dos", "Tres"]
# texto = "".join( lista )
# A la izquierda del .join() se indica el string con el cual unir los elementos como por ejemplo ", ".
# Si utilizamos un string vacío no intercala ningún carácter entre los elementos.

# textUser = input("Enter a text: ")
# firstIndex = int(input("Enter first index: "))
# secondIndex = int(input("Enter second index: "))
# length = len(textUser)
# while (firstIndex < -length) or (secondIndex < -length) or (firstIndex >= length) or (secondIndex >= length):
#     print("Invalid Index")
#     firstIndex = int(input("Enter first index: "))
#     secondIndex = int(input("Enter second index: "))
# reverseList = list(textUser)
# reverseList[firstIndex], reverseList[secondIndex] = reverseList[secondIndex], reverseList[firstIndex]
# reverseText = "".join(reverseList)
# print(reverseText)

# Mini-desafío: Operaciones sobre una lista
# Realizar un programa que ordena nombres alfabéticamente.
# Primero debe pedir al usuario que ingrese la cantidad de nombres que serán ingresados.
# Luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada.
# Dichos nombres deben ir agregándose a una lista. Por último, ordenar la lista alfabéticamente y mostrar
# en pantalla de a uno por vez los nombres ordenados.

# amountNames = int(input("How many names? "))
# allNames = list()
# while amountNames <= 0:
#     print("invalid amount")
#     amountNames = int(input("How many names? "))

# while amountNames > 0:
#     name = input("enter a name: ")
#     allNames.append(name)
#     amountNames -= 1
# allNames.sort()
# for x in allNames:
#     print(x)
