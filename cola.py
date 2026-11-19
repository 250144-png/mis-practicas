from collections import deque
import time

cola_turnos = deque()

cola_turnos.append(("A01", "Wero Palmas"))
cola_turnos.append(("A02", "Adrain Calvo"))
cola_turnos.append(("A03", "Benito Camelo"))

print("Turnos emitidos en la fila del banco:")

for turno, cliente in cola_turnos:
    print(f"Turno {turno} - {cliente}")

print("\nAtención en ventanilla\n")

while cola_turnos:

    turno, cliente = cola_turnos.popleft()

    print(f"Llamando a ventanilla: Turno {turno} - {cliente}")

    time.sleep(1)

    print(f"Atención finalizada: Turno {turno} - {cliente}")

    print(f"   (Clientes restantes en la fila: {len(cola_turnos)})\n")

print("Se han atendido todos los turnos. Fila vacía.")