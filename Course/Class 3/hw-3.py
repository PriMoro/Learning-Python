# Desafío a Entregar: Las Elecciones
# Los desafíos se entregan mediante esta página de HackerRank. Pueden ver un instructivo acerca del uso de la plataforma en este link.

# Realizar un programa en el cual se decida el ganador de unas elecciones.

# El programa primero recibe un número  N , la cantidad de votos totales que se realizaron. Luego recibe  N  votos en formato string,
# cada uno consiste en el nombre del candidato seleccionado.
# El programa debe calcular el ganador e imprimir su nombre. Para este ejemplo se asume que no hay empates.
# Los nombres y la cantidad de candidatos es desconocida.

# Ejemplo:

# Input:

# 12
# Mickey
# Donald
# Mickey
# Minnie
# Mickey
# Goofy
# Daisy
# Goofy
# Goofy
# Minnie
# Goofy
# Donald
# Output:

# Goofy
# El resultado es Goofy ya que este recibe 4 votos, la cual es la mayor cantidad de votos.

print("Please Insert a Number")
n = int(input())
number = n
dictionary_demo = {}
while number != 0:
    print("Insert a Name")
    name = input()
    name = name.lower()
    dictionary_demo[name] = dictionary_demo.get(name, 0) + 1
    number -= 1
winner = max(dictionary_demo, key=dictionary_demo.get)
print(dictionary_demo)
print(winner.capitalize())


# print(dictionary_demo)
