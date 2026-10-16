print("===tienda de videojuegos===")
cantidad = int(input("Ingrese la cantidad de videojuegos que desea comprar: "))
total = 0

for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del videojuego {i+1}: "))
    total = total + precio

descuento = 0

if total > 1000:
    descuento = total * 0.10
    print("Se aplicó un descuento del 10%.")

total_final = total - descuento

print(f"Subtotal: ${total:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total final a pagar: ${total_final:.2f}")
print("Gracias por su compra.")