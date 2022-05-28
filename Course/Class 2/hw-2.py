# #
# Desafío a Entregar: Ahorcado

# Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y
# otro jugador intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree
# que se encuentra en la palabra elegida. Una vez que el segundo jugador adivina todas las letras que se
# encuentran en la palabra, el juego termina y se muestra la cantidad de intentos que fueron necesarios.
# En esta versión del juego, si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias
# cuentan como adivinadas. Primero se recibe la palabra que se debe adivinar (por defecto vendrá en mayúsculas).
# Luego se reciben cierta cantidad de letras, una por línea, sin repetir. (por defecto vendrán en mayúsculas).
# Una vez que se haya adivinado la palabra del ahorcado, ya no se recibirán más letras. Su tarea es determinar
# la cantidad de intentos que fueron necesarios para adivinar la palabra completa, e imprimir ese número.

# Challenge (No se entrega en la corrección automática):

# Agregar una condición de perder, en el caso de que se haya superado cierta cantidad de intentos.
# Mostrar un contador de letras incorrectas, incrementarlo si la letra no esta en la palabra.
# Mostrar la palabra con guiones bajos _ en donde haya una letra que el jugador todavía no adivinó y mostrar las letras que sí adivinó.
# Por ejemplo, para la palabra AHORCADO debe mostrar: A _ O _ _ A _ O si el jugador ya ingreso las letras A, O y P.
# Armar una representación de la persona ahorcada del juego usando Arte ASCII, si prefieren pueden usar los dibujos ya creados
# por otras personas en internet.

print("Welcome! This is my Hangman Game")
print("You have 10 attempts to guess the word")
word = input("Word: ").upper()
while " " in word or len(word) == 0:
    print("ERROR! Delete blanks spaces")
    word = input("Word: ").upper()
lettersList = list()
for x in word:
    if x in lettersList:
        print(x)
    else:
        print("_")
letter = input("Letter: ").upper()
correctLetters = list()
incorrectLetters = list()
counter = 0
attempts = 0
length = len(word)

while counter < length and attempts < 10:
    if attempts == 9:
        print("Be careful! You have one last try")
    if letter in lettersList:
        print("Letter already chosen")
    elif len(letter) == 1 and letter in word:
        print("Good!")
        sum = word.count(letter)
        counter = counter + sum
        attempts += 1
        lettersList.append(letter)
        correctLetters.append(letter)
    else:
        print("Try Again!")
        attempts += 1
        lettersList.append(letter)
        incorrectLetters.append(letter)
    if counter != len(word):
        for x in word:
            if x in lettersList:
                print(x)
            else:
                print("_")
        letter = input("Letter: ").upper()
        print("Attempts: ", attempts)
if attempts >= 10:
    print("Game Over! You'll get it next time")
else:
    print("You do it! You're great player!")
    print("WORD: ", word)
    print("Total Attempts: ", attempts)
