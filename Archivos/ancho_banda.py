# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:34:55 2025

@author: Rafael
"""

import csv
archivo_csv = open("E:/Proyectos/py/ejercicios_diplo/Archivos/dns.csv")
archivo = csv.reader(archivo_csv, delimiter=';')
log_file = open("E:/Proyectos/py/ejercicios_diplo/Archivos/consumo_bandwidth.log", "w")
for f in archivo:
    ip1=f[0]
    oficina=f[1]
    trafico=0
    
    archivo_csv2 = open("E:/Proyectos/py/ejercicios_diplo/Archivos/trafico.csv")
    archivo2 = csv.reader(archivo_csv2, delimiter=';')
    for f2 in archivo2:
        ip2=f2[0]
        consumo=int(f2[1])
        if ip1 == ip2:
            trafico+=consumo
    archivo_log=f"La ip {ip1} tiene un consumo de ancho de banda de {trafico}\n"
    print(archivo_log)
    log_file.write(archivo_log)
    
archivo_csv.close()
archivo_csv2.close()
log_file.close()