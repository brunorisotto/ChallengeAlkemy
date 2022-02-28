import os
from settings import RUTA_CSV
from datetime import date

def guarda_dataset(archivo):

    if archivo == 'cine.csv':
        
        carpeta_cine = os.path.join(RUTA_CSV, "cine")

        if not os.path.exists(carpeta_cine):
            os.makedirs(carpeta_cine)

        carpeta_añomes = os.path.join(carpeta_cine,
                            date.today().strftime("%Y-%b"))
        
        if not os.path.exists(carpeta_añomes):
            os.makedirs(carpeta_añomes)
        
        ruta = os.path.join(carpeta_añomes, 'cine'+date.today().strftime("-%d-%m-%Y")+'.csv')
        
    if archivo == 'museo.csv':
        
        carpeta_museo = os.path.join(RUTA_CSV, "museo")

        if not os.path.exists(carpeta_museo):
            os.makedirs(carpeta_museo)

        carpeta_añomes = os.path.join(carpeta_museo,
                            date.today().strftime("%Y-%b"))
        
        if not os.path.exists(carpeta_añomes):
            os.makedirs(carpeta_añomes)
            
        ruta = os.path.join(carpeta_añomes, 'museo'+date.today().strftime("-%d-%m-%Y")+'.csv')
        
    if archivo == 'biblioteca_popular.csv':
        
        carpeta_biblioteca_popular = os.path.join(RUTA_CSV, "biblioteca_popular")

        if not os.path.exists(carpeta_biblioteca_popular):
            os.makedirs(carpeta_biblioteca_popular)

        carpeta_añomes = os.path.join(carpeta_biblioteca_popular,
                            date.today().strftime("%Y-%b"))
        
        if not os.path.exists(carpeta_añomes):
            os.makedirs(carpeta_añomes)
            
        ruta = os.path.join(carpeta_añomes, 'biblioteca_popular'+date.today().strftime("-%d-%m-%Y")+'.csv')
        
        
    return ruta
        