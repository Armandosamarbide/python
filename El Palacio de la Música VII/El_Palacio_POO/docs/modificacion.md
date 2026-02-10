# Modificación de un disco (modificacion.py)

Este módulo permite buscar un disco, editar sus detalles y guardarlo -o no- en la base de datos.

## Búsqueda del Disco

Se muestra un formulario de búsqueda con el título "Modificar Disco". Se debe ingresar el Título a modificar (el título debe ser exacto) y
presionar el botón "Buscar".

Si el campo está vacío, se muestra un mensaje de error pidiendo ingresar un título.

Si no se encuentra el disco buscado, se muestra un mensaje de error: "No se encontró ningún disco."

Si sí se lo encuentra, se carga el formulario de Modificación con los datos actuales del disco (Título, Artista, Año y Género).

## Modificación de la información

Se pueden editar campos sueltos o todos.

"Guardar cambios" envía la información editada a la base de datos, sobrescribiendo los datos antiguos. Si la modificación es exitosa, se muestra "Registro modificado." y vuelve a la pantalla de inicio.

"Cancelar" aborta la edición y regresa a la pantalla de inicio sin guardar ningún cambio. El registro queda con la información original.

Error Interno: Si la conexión a la base de datos falla durante el guardado, se mostrará un mensaje de error.

Importante: se deben revisarn los datos antes de pulsar "Guardar cambios", ya que la información anterior será reemplazada de forma
permanente.

