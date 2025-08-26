#Calcular el promedio de cada estudiante y determinar la nota mas alta

from datosEstudiantes import estudiantes


#Calcular el promedio de cada estudiante y determinar la nota mas alta

listaNotas =[]

for diccionario in estudiantes:
      print(diccionario["notas"])
      suma = sum( diccionario["notas"])
      listaNotas.append(suma)
      
print(listaNotas)

listaPromedios = []

for nota in listaNotas:
    promedio = round((nota/3), 2)
    listaPromedios.append(promedio)

print("Lista con todos los promedios de los estudiantes: ")
print(listaPromedios)

mejorProm = max(listaPromedios)
peorProm = min(listaPromedios)
print("El promedio mas alto es: ", mejorProm)
print("El promedio mas bajo es: ", peorProm)