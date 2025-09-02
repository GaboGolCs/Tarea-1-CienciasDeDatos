from datosEstudiantes import estudiantes    

contador = 0
for estudiante in estudiantes:
    for nota in estudiante["notas"]:
        if nota < 4.0:
            contador += 1
            break

total_estudiantes = len(estudiantes)
porcentaje = (contador / total_estudiantes) * 100
print(f"Porcentaje de estudiantes con al menos una nota menor a 4.0: {porcentaje:.2f}%")
