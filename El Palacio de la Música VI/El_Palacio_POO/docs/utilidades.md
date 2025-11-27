# Utilidades (utilidades.py y operaciones_misc.py)

Estos módulos agrupan las funciones de mantenimiento y control general de la interfaz de la aplicación. 

## Módulo Principal de Utilidades (utilidades.py)
Este módulo gestiona el estado y el cierre de la aplicación.

## Limpieza de la pantalla (limpiar_frame_center)
Prepara la sección central de la aplicación para mostrar un nuevo contenido.
Elimina todos los elementos que se estén mostrando en el panel central. Esto evita que los formularios se superpongan o que quede información antigua visible.

## Regresar al Inicio (mostrar_inicio)
Vuelve a la vista principal de la aplicación
Llama a la función de Limpieza de la Interfaz para dejar el panel central en blanco.

## Limpieza Total de Pantalla (limpiar_pantalla)
Limpia completamente el área de mensajes y el panel central.
Llama a la función Regresar al Inicio (mostrar_inicio) para limpiar el panel central.

## Cerrar la Aplicación (salir)
Termina la ejecución de la aplicación (root.destroy()).

## Módulo de Operaciones Misceláneas (operaciones_misc.py)
Este módulo llama a algunas funciones del módulo Utilidades.