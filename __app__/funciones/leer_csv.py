import pandas as pd
from funciones.encontrar_ruta import encuentra_ruta
from settings import RUTA_CSV
from datetime import date

# Funcion lee_csv, recibe String nombre de archivo, Boolean tieneIndice, List Indices


def lee_csv(archivo, tieneIndice, indices):

    if archivo == 'cine.csv':
        
        # se busca dataset actualizado en carpeta correspondiente 
        ruta_carpeta_cine = f'{RUTA_CSV}\cine'
        
        ruta_cine_csv = encuentra_ruta(archivo, ruta_carpeta_cine)
        
        
        # Si no tiene indices, lee csv sin parametro 'usecols'
        if not tieneIndice:
            lectura_df = pd.read_csv(ruta_cine_csv, header=0)
            
        # Si tiene indices, utiliza parametro 'usecols'
        else:
            lectura_df = pd.read_csv(ruta_cine_csv, header=0, usecols=indices)

    if archivo == 'museo.csv':
        
        ruta_carpeta_museo = f'{RUTA_CSV}\museo'
        
        ruta_museo_csv = encuentra_ruta(archivo, ruta_carpeta_museo)
        
        if not tieneIndice:
            lectura_df = pd.read_csv(ruta_museo_csv, header=0)
        else:
            lectura_df = pd.read_csv(ruta_museo_csv, header=0, usecols=indices)

    if archivo == 'biblioteca_popular.csv':
        
        ruta_carpeta_biblioteca_popular = f'{RUTA_CSV}'+r'\biblioteca_popular'
        
        ruta_biblioteca_popular_csv = encuentra_ruta(archivo, ruta_carpeta_biblioteca_popular)
        
        if not tieneIndice:
            lectura_df = pd.read_csv(ruta_biblioteca_popular_csv, header=0)
        else:
            lectura_df = pd.read_csv(ruta_biblioteca_popular_csv, header=0, usecols=indices)
    
    
    return lectura_df

