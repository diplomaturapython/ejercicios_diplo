import csv
archivo_csv = open("E:/Proyectos/py/ejercicios_diplo/Archivos/dns.csv")
archivo_csv2 = open("E:/Proyectos/py/ejercicios_diplo/Archivos/trafico.csv")
archivo = csv.reader(archivo_csv, delimiter=';')
archivo2 = csv.reader(archivo_csv2, delimiter=';')

for f in archivo:
    ip1=f[0]
    oficina=f[1]
    trafico=0
    for f2 in archivo2:
        ip2=f2[0]
        consumo=int(f2[1])
        if ip1 == ip2:
            trafico+=consumo
print(f"La ip {ip1} tiene un consumo de ancho de banda de {trafico}")

