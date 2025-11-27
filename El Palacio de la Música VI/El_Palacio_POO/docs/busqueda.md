# Búsqueda (busqueda.py)

Este módulo permite encontrar discos en la base de datos utilizando un término de búsqueda.

Al activar la función de búsqueda, se muestra una interfaz titulada "Búsqueda de disco".

Hay un solo campo de entrada: Título o Artista, donde se debe introducir la palabra clave o frase a buscar.

Al hacer click en "Buscar", se realiza una búsqueda en la base de datos:

Si no se ingresa texto en el campo, el sistema mostrará: "No se ingresó un término de búsqueda."

El sistema busca el término ingresado tanto en el campo Título como en el campo Artista. Esto significa que solo una parte del título o nombre del artista es suficiente para encontrar coincidencias.

## Resultados de la búsqueda

Si hay resultados, se muestran bajo el encabezado "Resultados de búsqueda:", listando la información completa de cada disco encontrado (ID, Título, Artista, Año, Género).

Si la búsqueda no arroja resultados, el panel de mensajes indicará: "No se encontraron registros que coincidan con la búsqueda solicitada."