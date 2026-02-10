## Aquí se registra la actividad de las funciones principales en el archivo log_actividad.txt

import os
from datetime import datetime
from log_cliente import enviar_log

def log_actividad(funcion):
    
    def dekorator(*args, **kwargs):
        nombre_funcion = funcion.__name__
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            resultado = funcion(*args, **kwargs)
            mensaje = f"[{fecha_hora}] Se ejecutó la función '{nombre_funcion}'."
            log_mensaje = mensaje + "\n"
        except Exception as e:
            mensaje = f"[{fecha_hora}] Función '{nombre_funcion}' falló. Error: {str(e)}"
            log_mensaje = mensaje + "\n"
            resultado = None
            
        print(mensaje)
        
        try:
            with open("log_actividad.txt", "a", encoding="utf-8") as archivo:
                archivo.write(log_mensaje)
        except Exception as io_error:
            print(f"Error al escribir en el log: {io_error}")

        enviar_log(log_mensaje)

        return resultado

    return dekorator
