# Matriz con datos
recursos = [
    ["Ana", 8, 8, 9, 8, 10],
    ["Carlos", 7, 8, 7, 8, 7],
    ["Luisa", 9, 9, 9, 9, 9],
    ["Pedro", 6, 7, 8, 7, 6]
]

# Función para calcular horas
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion

# Mostrar resultados
print("REPORTE SEMANAL")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print("-------------------")
    print("Nombre:", nombre)
    print("Total horas:", total)
    print("Clasificación:", clasificacion)