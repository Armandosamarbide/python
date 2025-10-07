import pandas as pd
dat_csv = pd.read_csv('empleados.csv', encoding = "ISO-8859-1", header = 0, usecols=['Cantidad','Precio'])
print(dat_csv.head())

# df = pd.read_csv('empleados.csv')
# print(df.head())

