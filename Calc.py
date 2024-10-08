import random
from itertools import combinations
import math

def generar_combinacion():
    # Generar 6 números únicos en el rango de 1 a 40
    numeros_principales = random.sample(range(1, 41), 6)

    # Generar un número extra en el rango de 1 a 12
    numero_extra_1 = random.choice(range(1, 13))

    # Generar un segundo número extra en el rango de 1 a 15
    numero_extra_2 = random.choice(range(1, 16))
    return numeros_principales, numero_extra_1, numero_extra_2

def mostrar_combinacion(numeros_principales, numero_extra_1, numero_extra_2):
    print("Números principales:", sorted(numeros_principales))
    print("Número extra 1:", numero_extra_1)
    print("Número extra 2:", numero_extra_2)

def ingresar_combinaciones_usuario():
    combinaciones_usuario = []
    print("Por favor ingresa 5 combinaciones:")
    for i in range(5):
        numeros_principales = []
        for j in range(6):
            num = int(input(f"Ingrese el número principal {j+1} para la combinación {i+1} (1-40): "))
            while num < 1 or num > 40 or num in numeros_principales:
                num = int(input(f"Número inválido o duplicado. Ingrese el número principal {j+1} para la combinación {i+1} (1-40): "))
            numeros_principales.append(num)

        numero_extra_1 = int(input(f"Ingrese el número extra 1 para la combinación {i+1} (1-12): "))
        while numero_extra_1 < 1 or numero_extra_1 > 12:
            numero_extra_1 = int(input(f"Número inválido. Ingrese el número extra 1 para la combinación {i+1} (1-12): "))

        numero_extra_2 = int(input(f"Ingrese el número extra 2 para la combinación {i+1} (1-15): "))
        while numero_extra_2 < 1 or numero_extra_2 > 15:
            numero_extra_2 = int(input(f"Número inválido. Ingrese el número extra 2 para la combinación {i+1} (1-15): "))

        combinaciones_usuario.append((numeros_principales, numero_extra_1, numero_extra_2))

    return combinaciones_usuario

def calcular_probabilidad_combinacion(combinacion_usuario, combinacion_generada):

    # Compara si la combinación generada coincide con alguna combinación del usuario
    return combinacion_usuario == combinacion_generada

def generador_de_combinaciones():
    combinaciones_usuario = ingresar_combinaciones_usuario()

    print("\nLas combinaciones ingresadas son:")
    for i, (numeros_principales, numero_extra_1, numero_extra_2) in enumerate(combinaciones_usuario):
        print(f"Combinación {i+1}:")
        mostrar_combinacion(numeros_principales, numero_extra_1, numero_extra_2)

    while True:
        # Generar una nueva combinación
        numeros_principales, numero_extra_1, numero_extra_2 = generar_combinacion()

        # Mostrar la combinación generada
        print("\nNueva combinación generada:")
        mostrar_combinacion(numeros_principales, numero_extra_1, numero_extra_2)

        # Verificar si la combinación generada coincide con alguna de las combinaciones ingresadas
        probabilidad = any(calcular_probabilidad_combinacion(
            (numeros_principales, numero_extra_1, numero_extra_2), 
            combinacion) for combinacion in combinaciones_usuario)

        if probabilidad:
            print("¡La combinación generada coincide con una de las combinaciones ingresadas!")

        else:
            print("La combinación generada no coincide con ninguna de las combinaciones ingresadas.")
        
        # Preguntar al usuario si desea generar otra combinación
        respuesta = input("¿Deseas generar otra combinación? (s/n): ")

        if respuesta.lower() != 's':
            break

# Ejecutar el generador de combinaciones
generador_de_combinaciones()
