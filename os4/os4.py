import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "img", "mascotas.jpg")
ruta = STATIC_ROOT + "\\mascotas.jpg"
print("-------------")
print(BASE_DIR)
print(STATIC_ROOT)
print(ruta)
print("-------------")
