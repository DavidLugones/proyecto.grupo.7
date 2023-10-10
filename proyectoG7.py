#Proyecto G 7 
#Alumnos:

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