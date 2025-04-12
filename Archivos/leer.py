import csv
archivo_csv = open("E:/Proyectos/py/ejercicios_diplo/Archivos/dns.csv")
archivo = csv.reader(archivo_csv, delimiter=';')
for f in archivo:
    print(f[0],f[1])
print("Fin de archivo")
