
import os
from datetime import datetime

def log_actividad(funcion):
    """
    Decorador para registrar la actividad de las funciones en un archivo de log.
    Registra el nombre de la función, la hora de ejecución y si fue exitosa o falló.
    """
    def envoltura(*args, **kwargs):
        nombre_funcion = funcion.__name__
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            resultado = funcion(*args, **kwargs)
            mensaje = f"[{fecha_hora}] Función '{nombre_funcion}' ejecutada con éxito."
            log_mensaje = mensaje + "\n"
        except Exception as e:
            mensaje = f"[{fecha_hora}] Función '{nombre_funcion}' falló. Error: {str(e)}"
            log_mensaje = mensaje + "\n"
            resultado = None  # O manejar la excepción como se prefiera
            # Re-lanzamos la excepción si queremos que el programa original la maneje
            # raise e 
            # Nota: En este caso, dada la estructura de try-except dentro de las funciones originales,
            # el decorador podría envolver todo, pero las funciones originales ya tienen sus bloques try-except.
            # Si decoramos los métodos que contienen la lógica, el decorador se ejecutará.
            
        print(mensaje) # Muestra en consola
        
        # Guardar en archivo
        try:
            with open("log_actividad.txt", "a", encoding="utf-8") as archivo:
                archivo.write(log_mensaje)
        except Exception as io_error:
            print(f"Error al escribir en el log: {io_error}")

        return resultado

    return envoltura
