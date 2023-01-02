import os
from datetime import date
from pathlib import Path
import re
from tabulate import tabulate
import time


rutaa = os.chdir('E:\\Mi_Gran_Directorio') #esta es la madre principa /ruta

patron = r'\w{4}-\d{5}'

lista = []

inicio = time.time()
for ruta, directorio, archivo in os.walk(".",topdown=True):

    for name in archivo:
      rt_actual = os.path.join(ruta, name)
      print(rt_actual)
      huevo = os.getcwd()
      #print("antes",huevo)
      huevo += rt_actual
      #print("despues",huevo)
      #print("name es",name)
      #print("estooo" , huevo)

      with open(huevo,'r') as f:
        sd = f.read()
        #print(sd)
        yu = re.search(patron,sd)
    
        if yu:
          print("yu es", yu.group())
          grupo = name,yu.group()
          lista.append(grupo)
          #lista.append(yu.group())

    for name in directorio:
      print(os.path.join(ruta, name))

final = time.time()
archivosen = tabulate(lista,headers =['  ARCHIVO','NRO. SERIE'])

si_esta = f"""
----------------------------------------------------
Fecha de búsqueda: {date.today()}

{archivosen}

Números encontrados: {len(lista)}
Duración de la búsqueda: {final-inicio}
----------------------------------------------------
"""

print(si_esta)