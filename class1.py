# Class 1

# nombre = "Priscila"
# edad = 19
# print(nombre, "tiene", edad, "años")

# input is interpreted as a text -- int(input()) is used to convert  input to integer
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# print("nombre:", nombre)
# print("edad:", edad)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Mini-desafío: Operadores
# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se muestre a la salida el promedio de los tres números.
# x = int(input("enter a number: "))
# y = int(input("enter a number:"))
# z = int(input("enter a number: "))

# average = (x + y + z)/3
# print(average)

# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se muestre a la salida la media geométrica de los tres números.
# x = int(input("enter a number: "))
# y = int(input("enter a number:"))
# z = int(input("enter a number: "))

# media = (x * y * z) ** (1/3)
# print(media)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Mini-desafío: Módulos
# hour = int(input("enter your hour: "))
# if hour > 24:
#     x = hour - 24
#     if x == 24:
#         print("Como tarda", hour, "horas", "llega a las", '00:00')
#     elif x == 1:
#         print("Como tarda", hour, "horas", "llega a la", '01:00')
#     else:
#         print("Como tarda", hour, "horas", "llega a las", x, ':00')
# else:
#     if hour == 24:
#         print("Como tarda", hour, "horas", "llega a las", '00:00')
#     elif hour == 1:
#         print("Como tarda", hour, "horas", "llega a la", '01:00')
#     else:
#         print("Como tarda", hour, "horas", "llega a las", hour, ':00')

# ____________________________

# Mini-desafío: if
# Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4)
# utilizando un if/else. La nota será ingresada por el usuario usando input().
# mark = int(input("enter your mark: "))

# if mark >= 4:
#     print("Passed")
# else:
#     print("Failed")
# Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F
# de acuerdo a la siguiente conversión:
# numberToConvert = int(input("enter a number of 0 until 100: "))
# if numberToConvert <= 100 and numberToConvert > 89:
#     print("A")
# elif numberToConvert <= 89 and numberToConvert > 79:
#     print("B")
# elif numberToConvert <= 79 and numberToConvert > 69:
#     print("C")
# elif numberToConvert <= 60 and numberToConvert > 59:
#     print("D")
# elif numberToConvert <= 59 and numberToConvert >= 0:
#     print("F")
# else:
#     print("There aren't letters to this number")

# Mini-desafío: while
# Implementar un programa que reciba 2 números (A y B), y luego imprima en pantalla
# la secuencia de números enteros desde A hasta B.
# En el caso de que B sea menor que A, se debe repetir el pedido de B hasta que sea válido ( B  ≥  A ).

# numberA = int(input("enter a number: "))
# numberB = int(input("enter another number: "))

# while numberB <= numberA:
#     print("please, remember that you have to enter valid numbers, try again")
#     numberB = int(input("enter another number: "))

# while numberA < numberB:
#     print(numberA)
#     numberA += 1

# print(numberB)

# Implementar un programa que muestre la siguiente secuencia:

# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0

# count = 0
# sum = 0

# while (sum >= 1 or sum < 5) and count < 10:
#     if count >= 5:
#         sum -= 1
#         print(sum)
#         count += 1
#     else:
#         sum += 1
#         print(sum)
#         count += 1

# print("count:", count)

# Mini-desafío: for
# Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado.
# Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. Luego, para cada producto,
# se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo.
# Posteriormente el programa imprimirá dicho código.

# productCode = int(input("Enter product code: "))
# amount = int(input("Enter number of times to print it: "))

# numberOfProducts = int(input("Products need a tag: "))
# for x in range(numberOfProducts):
#     productCode = int(input("Enter product code: "))
#     amount = int(input("Enter number of times to print it: "))
#     for x in range(amount):
#         print(productCode)

# Mini-desafío: Funciones
# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan
# Contraseña: 12345_

# Usuario: Pablo
# Contraseña: xDcFvGbHn

# La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.

# def checkLogIn(user, password):
#     if (user == "Juan" and password == "12345_") or (user == "Pablo" and password == "xDcFvGbHn"):
#         logIn = True
#     else:
#         logIn = False
#     return logIn


# logUser = input("enter user: ")
# logPassword = input("enter password: ")

# while not checkLogIn(logUser, logPassword):
#     print("Incorrect data. Please, try again")
#     logUser = input("enter user: ")
#     logPassword = input("enter password: ")
# else:
#     print("Logged successfully")

# Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.

# Ejemplos:

# contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)

# contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)

# def divisors(n):
#     count = 1
#     aux = n
#     while aux != 1:
#         if n % aux == 0:
#             count += 1
#         aux -= 1
#     return (count)

# print(divisors(9))
# print(divisors(10))
# print(divisors(2))
# print(divisors(13))
# print(divisors(20))
