#Entrega un listado ordenado de mayor a menor con el promedio de los estudiantes
from datosEstudiantes import estudiantes

listaNotas =[]

for diccionario in estudiantes:
      suma = sum( diccionario["notas"])
      listaNotas.append(suma)
      

listaPromedios = []

#Obtenemos la lista con las notas y las aproximamos
for nota in listaNotas:
    promedio = (nota/3) #obtenemos el promedio
    promedio = round(promedio, 2) #Aproximamos a 2 decimales
    listaPromedios.append(promedio) #Agregamos al promedio de la lista


#Invertimos la lista de mayor a menor
listaPromedios.sort(reverse=True)
print("La lista ordenada de mayor a menor:")
print(listaPromedios)