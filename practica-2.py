#quiero hacer un sistema de calificaciones, que solicite 5 aplicaciones, 
# los guarde en una lista, calcule y coloque el promedio y muestre la calificacion mas alta

# -*- coding: utf-8 -*-

calificaciones = []
for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
calificacion_alta = max(calificaciones)

print(f"El promedio es: {promedio}")
print(f"La calificación más alta es: {calificacion_alta}")



