print("===tienda de videojuegos===")
cantidad = int(input("Ingrese la cantidad de videojuegos que desea comprar: "))
total = 0
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del videojuego {i+1}: "))      
    total = total + precio