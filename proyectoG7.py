#Proyecto G 7 
#Alumnos:
<<<<<<< HEAD

import random

palabras = ["septima", "programacion", "boca juniors", "ahorcado"]

ahorcado = random.choice(palabras)

adivinadas = []
incorrectas = []
intentos = 6
intentos_restantes = intentos

while intentos_restantes > 0:
    print("Palabra: " + " ".join(letra if letra in adivinadas else "_" for letra in ahorcado))
    print("Letras incorrectas: ", " ".join(incorrectas))
    print("Intentos restantes: " ,intentos_restantes)
    
    
    letra = input("Ingresa una letra: ").lower()
    
    if letra.isalpha() and len(letra) == 1:
        if letra in adivinadas or letra in incorrectas:
            print("Letra repetida, ingrese otra letra.")
        elif letra in ahorcado:
            adivinadas.append(letra)
            
            if set(adivinadas) == set(ahorcado):
                print("Adivinaste la palabra: ",ahorcado)
        else:
            incorrectas.append(letra)
            intentos -= 1
=======
#Alumnos:Juan Pablo Zarza,Fernando Tomás Burgos
import random

# Función para seleccionar una palabra aleatoria de la lista
def seleccionar_palabra():
    palabras = ["python", "programacion", "informatorio", "boca", "septima", "ahorcado"]
    return random.choice(palabras)

# Función para inicializar el juego y establecer las variables iniciales
def inicializar_juego():
    palabra_secreta = seleccionar_palabra()
    intentos_restantes = 6
    letras_adivinadas = []
    letras_incorrectas = []
    return palabra_secreta, intentos_restantes, letras_adivinadas, letras_incorrectas

# Función para mostrar el estado actual del juego
def mostrar_estado(palabra_secreta, letras_adivinadas, letras_incorrectas, intentos_restantes):
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    print("Palabra: " + palabra_mostrada)
    print("Letras incorrectas: " + ", ".join(letras_incorrectas))
    print("Intentos restantes: " + str(intentos_restantes))
>>>>>>> b3fc1be8899984cb03dfb9bc6eddd699261785f0
