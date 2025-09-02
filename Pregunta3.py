import statistics

from datosEstudiantes import estudiantes

notas_curso = []
for estudiante in estudiantes:
    for nota in estudiante["notas"]:
        notas_curso.append(nota)

moda = statistics.multimode(notas_curso)
print("La nota mas frecuente (moda) considerando todos los estudiantes es", moda)

