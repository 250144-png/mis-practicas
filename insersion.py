import matplotlib.pyplot as plt 

datos = [42, 12, 88, 23, 7, 65, 34, 50]

# Algoritmo de Inserción
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if a[j] > clave:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = clave
    return a, comp

# Algoritmo de Selección
def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, comp

# Ejecutamos los dos algoritmos
lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)

# Graficación con matplotlib
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Gráfico 1: Lista original
ax1.bar(range(len(datos)), datos, color='red')
ax1.set_title('1. Lista Original')
ax1.set_ylabel('Valor')

# Gráfico 2: Lista ordenada
ax2.bar(range(len(datos)), lista_ordenada, color='blue')
ax2.set_title('2. Lista Ordenada')

# Gráfico 3: Comparaciones realizadas
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_sel], color=['orange', 'green'])
ax3.set_title('3. Comparaciones')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show()