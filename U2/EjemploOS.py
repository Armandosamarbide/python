## Ejemplo de cómo encontrar archivos

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(BASE_DIR, "www.YTS.MX.jpg")

print(ruta)