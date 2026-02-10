# Añadir un nuevo disco (alta.py)

Este módulo proporciona una interfaz visual para que el usuario agregue una nueva entrada -nuevo disco- y guardarla de forma permanente en la base de datos de la aplicación.

## Alta de un nuevo registro

Al activar esta opción, primero se limpia cualquier contenido del área central. A continuación, se muestra un formulario sencillo con el título "Dar de alta un nuevo disco" y los siguientes campos de texto para la entrada de datos:

Título: Nombre del álbum/disco.
Artista: Nombre del artista o banda.
Año: Año de lanzamiento.
Género: Género musical al que pertenece el disco.

Al final del formulario, se presenta el botón "Guardar".

Al clickear en "Guardar", se verifica que los campos Título y Artista contengan solo letras, números y espacios. Se rechazarán otros caracteres (como símbolos especiales o puntuación excesiva). Si la verificación falla, se muestra un mensaje de error indicando "Error en los campos Título o Artista", y el registro no se guarda.

Caso contrario, la aplicación conecta con la base de datos e inserta todos los datos proporcionados en la tabla de discos.

## Validación del guardado en la BBDD

Si el guardado es exitoso, se muestra un mensaje en el panel de resultados que confirma la acción, por ejemplo: "Registro agregado: ('Nombre del disco', 'Artista', 'Año', 'Género')".

Si hay algún problema interno al intentar guardar (Base de datos no disponible o error de conexión), se informará al usuario con un mensaje de error detallado en el panel de resultados.

Una vez finalizado el proceso, se cierra la conexión con la base para ahorrar recursos.