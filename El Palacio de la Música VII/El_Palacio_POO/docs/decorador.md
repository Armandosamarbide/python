# Decorador (decoradores.py)

Este módulo proporciona herramientas para la creación de logs de las funciones principales del sistema.

## Función principal

Es un decorador que se utiliza para envolver otras funciones y registrar cuándo se ejecutan y si se ejecutaron correctamente o fallaron.

## ¿Qué hace?



1\. Registra el nombre de la función y la fecha y hora a la que se ejecutó.

2\. Si la función falla, captura el error y lo guarda en el log sin detener el programa.

3\. Muestra un mensaje en la terminal indicando el estado de la ejecución.

4\. Los mensajes se guardan en un archivo llamado 'log\_actividad.txt'.

5\. Envía el log mediante la función 'enviar\_log' del módulo 'log\_cliente'.



