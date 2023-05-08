"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En has sacado donde es 
 cada una des las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario."""
 
materias = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
calificaciones=[]
for materia in materias:
    calificacion = input("¿Que calificacion has sacado en " + materia + "?")
    calificaciones.append(calificacion)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + calificaciones[i])