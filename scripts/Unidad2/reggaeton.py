import random

mujeres = ["Mami","Baby","Chica","Zorra"]

acciones = ["yo quiero", "vamos a","voy a", "vengo a"]

hacer = ["castigarte", "darte", "azotarte"]

adjetivos = ["duro", "lento", "suave", "fuerte"]

tiempos = ["toda la noche", "hasta mañana", "hasta que digas basta"]

formas = ["sin anestesia", "en el piso", "contra la pared"]


mujer = random.sample(mujeres,1)[0]

accion = random.sample(acciones,1)[0]

hago = random.sample(hacer,1)[0]

adjetivo = random.sample(adjetivos,1)[0]

tiempo = random.sample(tiempos,1)[0]

forma = random.sample(formas,1)[0]


print(mujer + " " + accion + " " + hago + " " + adjetivo + " " + tiempo + " " + forma )