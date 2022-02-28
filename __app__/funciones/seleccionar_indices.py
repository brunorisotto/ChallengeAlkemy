
# Retorna indices correspondientes de cada DataFrame
def buscar_indices(dic, columna_df):

    indices = []
    clave_dic = list(dic.values())

    for indice_dic in clave_dic:
        for indice_df in columna_df:
            if indice_dic == indice_df:
                indices.append(columna_df.index(indice_df))

    return indices
