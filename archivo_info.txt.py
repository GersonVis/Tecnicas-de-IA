# coding: utf-8
## la columna id ya contiene un indice de datos podemos sobreescribri el indice a ocupar
## sintaxis: pandas.read_csv(nombre_del_archivo.csv, index_col="nombre_de_la_columna")
data_con_columa=pd.read_csv("informacion.csv", index_col='id')
data_con_columa
