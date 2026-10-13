# Punto 1: tabla de multiplicar del 1 al 10


def pedir_entero():
    while True:
        texto = input("Ingresa un numero entero: ").strip()
        try:
            # int valida que el texto sea un entero, por ejemplo 7 o -3.
            return int(texto)
        except ValueError:
            print("Entrada no valida. Debes ingresar un numero entero (por ejemplo, 5). Intenta otra vez.")


def ejecutar():
    print("\n--- TABLA DE MULTIPLICAR ---")
    numero = pedir_entero()
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    input("\nPresiona Enter para volver al menu...")


if __name__ == "__main__":
    ejecutar()
