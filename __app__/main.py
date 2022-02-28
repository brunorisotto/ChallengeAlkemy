import scrapper
from settings import RUTA_CONEXION_SQL


from funciones.buscar_diccionario import *
from funciones.seleccionar_indices import buscar_indices
from funciones.limpieza_datos import cambiar_a_nulos
from funciones.leer_csv import lee_csv
from funciones.renombrar_columnas import renombra_columnas
from funciones.cargar_sql import cargar_df_a_sql
from funciones.conexion_sql import conexion
from funciones.operaciones_sql import *
from loggers import logger_debug, logger_error
from datetime import datetime

global connex_sql

try:
    
    # Obtencion de conexion a DB
    connex_sql = conexion(RUTA_CONEXION_SQL)
    
    logger_debug.debug("Conexion a Database exitosa.")
    
    # Se borran las tablas de DB si existen
    
    eliminar_tabla_normalizada(connex_sql)
    eliminar_tabla_registro(connex_sql)
    eliminar_tabla_cine(connex_sql)
    
except Exception as e:
            logger_error.error(e)


nombres_dataset = ['museo.csv',
                   'cine.csv',
                   'biblioteca_popular.csv']

# Fecha hoy
fecha_hoy = datetime.today().strftime('%d-%m-%Y')

try:
    
    for archivo in nombres_dataset:

        tieneIndice = False
        normalizado_indices = []

        df = lee_csv(archivo, tieneIndice, normalizado_indices)
        logger_debug.debug(f"Dataset: {archivo} crudo leido con exito.")

        if archivo == 'cine.csv':
            
            dic_cine = buscar_dic_cine(archivo)
            df_cine = renombra_columnas(df, dic_cine)
            cine_indices = buscar_indices(dic_cine, df_cine.columns.tolist())

        # Buscar indices para generar tablas

        dic_normalizado = buscar_dic_normalizado(archivo)
        df_normalizado = renombra_columnas(df, dic_normalizado)
        normalizado_indices = buscar_indices(
            dic_normalizado, df_normalizado.columns.tolist())

        dic_registro = buscar_dic_registro(archivo)
        df_registro = renombra_columnas(df, dic_registro)
        registro_indices = buscar_indices(
            dic_registro, df_registro.columns.tolist())

        if normalizado_indices != []:
            
            tieneIndice = True

            # Lee nuevamente el DATASET con las columnas a utilizar para generar tablas

            df_normalizado = lee_csv(archivo, tieneIndice, normalizado_indices)
            df_normalizado = renombra_columnas(df_normalizado, dic_normalizado)
            df_normalizado['fecha_carga'] = fecha_hoy

            df_registro = lee_csv(archivo, tieneIndice, registro_indices)
            df_registro = renombra_columnas(df_registro, dic_registro)
            df_registro['fecha_carga'] = fecha_hoy

            if archivo == 'cine.csv':
                
                df_cine = lee_csv(archivo, tieneIndice, cine_indices)
                df_cine = renombra_columnas(df_cine, dic_cine)
                df_cine['fecha_carga'] = fecha_hoy
                cambiar_a_nulos(df_cine)
                
            logger_debug.debug(f"Dataset: {archivo} con columnas necesarias leido con exito.")

            # Limpieza de datos no proporcionado por la fuente
            cambiar_a_nulos(df_normalizado)
            cambiar_a_nulos(df_registro)
            
        

        # Introduccion de datos a tablas correspondientes

        if archivo == 'cine.csv':

            cargar_df_a_sql(df_cine, "tabla_cine_apoyo", connex_sql)
            logger_debug.debug(f"Se ha insertado {archivo} correctamente a tabla: tabla_cine_apoyo.")

        cargar_df_a_sql(df_normalizado, "tabla_normalizada", connex_sql)
        logger_debug.debug(f"Se ha insertado {archivo} correctamente a tabla: tabla_normalizada.")
        

        cargar_df_a_sql(df_registro, "tabla_registro_apoyo", connex_sql)
        logger_debug.debug(f"Se ha insertado {archivo} correctamente a tabla: tabla_registro_apoyo.")
    
    logger_debug.debug(f"---------- Se ha creado exitosamente a tabla: tabla_normalizada ----------")
    
except Exception as e:
    
        logger_error.error(e)

# Generar tabla registro, tabla cine con la informacion procesada correspondiente

crear_tabla_registro(connex_sql)
logger_debug.debug(f"---------- Se ha creado exitosamente la tabla: tabla_registro ----------")

crear_tabla_cine(connex_sql)
logger_debug.debug(f"---------- Se ha creado exitosamente la tabla: tabla_cine ----------")

# Eliminar tabla registro, tabla cine de apoyo
eliminar_tabla_registro_apoyo(connex_sql)
logger_debug.debug(f"Se ha eliminado la tabla de apoyo : tabla_registro_apoyo.")

eliminar_tabla_cine_apoyo(connex_sql)
logger_debug.debug(f"Se ha eliminado la tabla de apoyo : tabla_cine_apoyo.")

logger_debug.debug(f"---------- El programa ha terminado ----------")
