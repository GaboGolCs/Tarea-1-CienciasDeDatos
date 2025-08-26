#Cuantos estudiantes aprobaron todas las asignaturas todas las notas >= 4.0

from datosEstudiantes import estudiantes


sinRamoReprobado = len(estudiantes)
listaNotas = []
indice = 0;

#Lleno la lista de notas con las notas en cada diccionario
for diccionario in estudiantes:
    listaNotas.append(diccionario["notas"])

#listaDeNotas es una luista que contiene cada lista de notas de cada estudiante
for notasEstudiante in listaNotas:
    for nota in notasEstudiante: #comparo cada nota en cada casilla de un estudiante en paricular
        if(nota<4.0):
            sinRamoReprobado -=1 #Cada vez que se encuentra que un estudiante tiene una nota bajo 4 entonces se resta 1
            break
          
print(sinRamoReprobado)

    

