import csv
import random
import interfaz

# Funcion leer el archivo .csv y elijo una palabra de este.
def leer_palabra_secreta():
    with open('palabras.csv') as csvfile:
      lista = list(csv.DictReader(csvfile))
      diccionario = random.choice(lista)
      palabra_aleatoria = diccionario['palabras']
      print(palabra_aleatoria)
      return palabra_aleatoria 


#Funcion pedir letra, esta función hace que el jugador ingrese solo una letra.
def pedir_letra(letras_usadas):
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        # verifica que se ingreso solo un caracter
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in letras_usadas:
            print ('Ya has elegido esa letra prueba con otra letra!!!')
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz':
            print ('Solo introduce letras!!!! Elije una letra!!!')
        else:
            letras_usadas.append(letra)
            return letra


# Funcion "verificar_letra"
def verificar_letra(letra, palabra_secreta):
   letrasencontradas = ''
   if letra in palabra_secreta:
        letrasencontradas = True
   else:
        letrasencontradas = False         
   return letrasencontradas 


# Funcion "validar_palabra"
def validar_palabra(letras_usadas, palabra_secreta):
    letras_encontradas = True
    for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_usadas:
                letras_encontradas = False
                break          
    return letras_encontradas          
          


#####################################
## Bloque principal del programa
#####################################

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del AHORCADO!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Funcion leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta()
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)
        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡GANO!¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡AHORCADO! ¡FIN DEL JUEGO!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')            


    