import pandas as pd
import numpy as np

# retorna DataFrame con datos sin informacion como nulos


def cambiar_a_nulos(df):

    for columna in df:
        flag_variable = df[columna] == 's/d'
        df.loc[flag_variable, columna] = np.nan

    return df
