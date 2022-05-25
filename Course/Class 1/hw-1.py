# Desafío a Entregar: La conjetura del Dr. Lothar
# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
# Si el número es par, se debe dividir por  2 .
# Si el número es impar, se debe multiplicar por  3  y sumar  1 .
# Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

# Ejemplos:

# Input: 6

# Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)

# Input: 13

# Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)

number = int(input("number: "))
count = 0
#stop = 1
print(int(number))
while number != 1:
    if number % 2 == 0:
        number = number / 2
        print(int(number))
        count += 1
    else:
        number = number * 3 + 1
        print(int(number))
        count += 1

print("total steps: ", count)
