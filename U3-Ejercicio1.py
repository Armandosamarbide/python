import pandas as pd
from matplotlib import pyplot as plt

dat = pd.read_excel("temperaturas.csv")
print(dat)
print(dat.dia)
print(dat.temperatura)

x = dat.dia
y = dat.temperatura
plt.plot(x,y)
plt.show()