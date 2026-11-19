import numpy as np

precio = 50

A = np.array([[10, 15], [20, 5]])  # Sabado
B = np.array([[5, 12], [15, 8]])   # Domingo

total = A + B
ingresos = total * precio

print("VENTAS CON NUMPY")
print("Total de productos vendidos:")
print(total)
print("Ingresos en pesos:")
print(ingresos)

# Con Python nativo
A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]

total = [[0, 0], [0, 0]]
ingresos = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        total[i][j] = A[i][j] + B[i][j]
        ingresos[i][j] = total[i][j] * precio

print("\nVENTAS CON PYTHON NATIVO")
print("Total de productos vendidos:")
for fila in total:
    print(fila)

print("Ingresos en pesos:")
for fila in ingresos:
    print(fila)
