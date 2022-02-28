import pandas as pd

# Funcion cargar_df_a_sql, introduce datos a DB


def cargar_df_a_sql(df, nombre_tabla, conexion):

    df.to_sql(nombre_tabla, con=conexion, if_exists="append")
