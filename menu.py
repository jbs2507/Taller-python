# Menu principal del taller
import juliana
import daniela
import emanuel


def mostrar_menu():
    while True:
        print("\n========== MENU DEL TALLER ==========")
        print("1. Tabla de multiplicar (Juliana)")
        print("2. Adivina el número (Daniiela)")
        print("3. Separar números pares e impares (Emanuel)")
        print("4. Salir")
        print("=====================================")

        opcion = input("Selecciona una opcion (1-4): ").strip()

        if opcion == "1":
            juliana.ejecutar()
        elif opcion == "2":
            daniela.ejecutar()
        elif opcion == "3":
            emanuel.ejecutar()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida. Ingresa solamente 1, 2, 3 o 4.")


if __name__ == "__main__":
    mostrar_menu()
