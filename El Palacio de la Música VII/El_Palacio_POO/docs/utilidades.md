# Utilidades (utilidades.py y operaciones\_misc.py)

Estos módulos agrupan las funciones de mantenimiento y control general de la interfaz de la aplicación.

## Módulo Principal de Utilidades (utilidades.py)

Este módulo gestiona el estado y el cierre de la aplicación.

## Limpieza de la pantalla (limpiar\_frame\_center)

Prepara la sección central de la aplicación para mostrar un nuevo contenido.
Elimina todos los elementos que se estén mostrando en el panel central. Esto evita que los formularios se superpongan o que quede información antigua visible.

## Regresar al Inicio (mostrar\_inicio)

Vuelve a la vista principal de la aplicación
Llama a la función de Limpieza de la Interfaz para dejar el panel central en blanco.

## Limpieza Total de Pantalla (limpiar\_pantalla)

Limpia completamente el área de mensajes y el panel central.
Llama a la función Regresar al Inicio (mostrar\_inicio) para limpiar el panel central.

## Cerrar la Aplicación (salir)

Termina la ejecución de la aplicación (root.destroy()).

## Módulo de Operaciones Misceláneas (operaciones\_misc.py)

Este módulo llama a algunas funciones del módulo Utilidades.

## Logging

Estos componentes permiten que la aplicación envíe mensajes de estado o alertas de errores a un servidor.

## server\_log.py

Monitorea la red y guarda en un archivo (log\_remoto.txt) la información que recibe.

## log\_cliente.py

Este componente envía los mensajes al servidor. Si el servidor no está funcionando, lo ignora para no paralizar la ejecución del programa.

## test\_logging.py

Manda mensajes de prueba al servidor.





## 

