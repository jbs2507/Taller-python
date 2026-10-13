# Punto 3: reemplaza el contenido de ejecutar() por el ejercicio de Emanuel.


def ejecutar():
    print("\n--- EJERCICIO 21: SEPARAR NÚMEROS PARES E IMPARES ---")

    numeros = []
    print("Ingresa 15 números enteros:")
    for i in range(1, 16):
        while True:
            try:
                num = int(input(f"  Número {i}: "))
                numeros.append(num)
                break
            except ValueError:
                print("  ⚠ Entrada no válida. Ingresa un número entero.")

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print(f"\nLista original: {numeros}")
    print(f"Pares ({len(pares)}):   {pares}")
    print(f"Impares ({len(impares)}): {impares}")

    input("\nPresiona Enter para volver al menú...")
