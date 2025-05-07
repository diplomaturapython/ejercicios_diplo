#Para abrir el archivo "lenguaje.txt" hacer lo siguiente:
archivo = open("Direccion donde esta el archivo", "r")
contenido = archivo.read()
print(contenido)
archivo.close()  #

#Rutina para escribir un archivo
archivo = open("nombre_archivo.txt", "w")
archivo.write("Texto de ejemplo\n")
archivo.close()

#Rutina para escribir el archivo al final de linea sin borrar lo anterior
archivo = open("nombre_archivo.txt", "a")# en vez de "w" se pone "a" que es para agregar al final del archivo a= append
archivo.write("Texto de ejemplo\n")
archivo.close()