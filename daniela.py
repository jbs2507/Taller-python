# Punto 19: Adivina el número


def ejecutar():
    print("\n--- EJERCICIO 19: ADIVINA EL NÚMERO ---")

    secreto = 13
    intentos = []
    acertado = False

    for i in range(5):
        numero = int(input("Intento " + str(i + 1) + " de 5. Adivine el número (1-20): "))
        intentos.append(numero)

        if numero == secreto:
            acertado = True
            print("¡Adivinaste!")
            break
        elif numero > secreto:
            print("El número secreto es menor")
        else:
            print("El número secreto es mayor")

    if not acertado:
        print("Perdiste, el número era", secreto)

    print("Tus intentos:", intentos)

    input("\nPresiona Enter para volver al menú...")
