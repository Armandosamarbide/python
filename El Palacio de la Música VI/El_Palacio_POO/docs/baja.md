# Borrar discos (baja.py)

Este módulo permite al usuario borrar un disco existente en la base de datos.

Al activar esta opción, el área central de la aplicación se limpia. Se muestra un formulario simple que permite buscar el disco a eliminar.

## Proceso de eliminación de registros

Al pulsar "Buscar", el sistema elimina el registro siguiendo estos pasos:

Primero, valida si el campo Título está vacío. En ese caso, se muestra el mensaje: "Debe ingresar un título."

El sistema busca en la base de datos un disco que coincida exactamente con el título ingresado.

Si no se lo encuentra, el panel mostrará un mensaje de error.

Si se encuentra el disco (o varios discos con el mismo título), el sistema procede a borrarlos de la base de datos. Se confirmará la operación con el mensaje: "Registro eliminado."

En caso de un problema de conexión o de base de datos, se informará con un mensaje de error técnico.

Importante: El sistema requiere el título exacto (respetando mayúsculas, minúsculas y espacios) para encontrar y eliminar el disco. Una vez eliminado, el registro no se puede recuperar.