# -*- coding: utf-8 -*-
# Cajero automático
saldo = 1000

print("=== CAJERO AUTOMÁTICO ===")

while True:
    print("\nMenu:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo} pesos")
    elif opcion == "2":
        cantidad = int(input("Ingresa la cantidad a retirar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif cantidad > saldo:
            print("No tienes suficiente saldo.")
        else:
            saldo -= cantidad
            print(f"Retiraste ${cantidad} pesos.")
            print(f"Saldo restante: ${saldo} pesos")
    elif opcion == "3":
        print("Gracias por usar el cajero automático.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")