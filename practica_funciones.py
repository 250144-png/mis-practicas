def mostrar_encabezado_escuela():
    print("UTXJ")
    print("Reporte")


def obtener_nota_minima_aprobatoria():
    return 7


def evaluar_rendimiento(nota_final):
    if nota_final < 7:
        return "Reprobado"
    elif nota_final < 9.4:
        return "Aprobado"
    else:
        return "Excelente"


def calcular_promedio_ponderado(nota_examen, nota_tareas):
    promedio = (nota_examen * .70) + (nota_tareas * .30)
    return round(promedio, 1)


def generar_boleta(nombre_alumno, nota_examen, nota_tareas):

    nota_final = calcular_promedio_ponderado(nota_examen, nota_tareas)

    nota_minima = obtener_nota_minima_aprobatoria()

    estado = evaluar_rendimiento(nota_final)

    print("\n BOLETA ")
    print("Nombre:", nombre_alumno)
    print("Nota del examen:", nota_examen)
    print("Nota de tareas:", nota_tareas)
    print("Nota final:", nota_final)
    print("Estado:", estado)

    if nota_final < nota_minima:
        print("Necesita presentar examen extraordinario: Sí")
    else:
        print("Necesita presentar examen extraordinario: No")



nombre = input("Ingresa el nombre del alumno: ")
nota_examen = float(input("Ingresa la nota del examen: "))
nota_tareas = float(input("Ingresa la nota de tareas: "))


generar_boleta(nombre, nota_examen, nota_tareas)