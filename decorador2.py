import logging

## Logging sirve para mostrar mensajes de información, errores y advertencias

from functools import wraps

## Wraps sirve para que la función decorada conserve su nombre y documentación original
## Sin él, python pensaría que SUMAR se llama WRAPPER

logging.basicConfig(level=logging.INFO)

## "Mostrame mensajes INFO o más importantes". Si no estuviera esto, los mensajes logging.info() no se verían

## Se define el decorador: una función que recibe otra función y entrega una función nueva.

## FUNC es SUMAR
## WRAPPER envuelve a la función original e intercepta su ejecución

def log_ejecucion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ejecutando {func.__name__} args={args} kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        logging.info(f"{func.__name__} finalizó correctamente")
        return resultado
    return wrapper

##

@log_ejecucion
def sumar(a, b):
    return a + b

sumar(3, 4)