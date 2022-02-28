import pandas as pd

# Retorna DataFrame correspondiente con columnas renombradas


def renombra_columnas(df, dic):

    df = df.rename(columns=dic)

    return df
