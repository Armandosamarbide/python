# Disquería "El Palacio de la Música" - POO Edition

## Descripción general del proyecto

El programa es una base de datos de discos , que permite realizar operaciones básicas de:

- Alta;
- Baja;
- Modificación;
- Consulta;

Más las funciones adicionales de limpieza de pantalla y salir del programa.

El menú está hecho con Tkinter. Es una interfaz intuitiva, con los botones situados a la izquierda y que permiten acceder a las funciones del programa. Los resultados de la ejecución de las funciones se muestran en la pantalla central, cuyo tamaño está definido inicialmente en 800X600.

## Archivos incluídos en el proyecto

    mkdocs.yml # Archivo de configuración de MKDOCS
    
    docs/
    index.md # Homepage de la documentación
    alta.md # Alta de un nuevo disco
    baja.md # Borrar un disco
    modificacion.md # Modificar un disco previamente cargado
    busqueda.md # Buscar registros
    mostrartodo.md # Listar todos los registros cargados
    utilidades.md # Funciones de control general.

    home/
    index.md # Homepage de la documentación
    Alta (alta.py) # Permite al usuario agregar una nueva entrada y guardarla de forma permanente en la BBDD.
    Baja (baja.py) # Permite al usuario borrar un disco existente en la BBDD.
    Modificación (modificacion.py) # Permite buscar un disco, editar sus detalles y guardarlo -o no- en la BBDD.
    Búsqueda (busqueda.py) # Permite encontrar discos en la BBDD utilizando un término de búsqueda.
    Listar todo (listartodo.py) # Este módulo muestra la lista completa de todos los discos registrados actualmente en la BBDD.
    Utilidades (utilidades.py, operaciones_misc.py) # Estos módulos agrupan las funciones de mantenimiento y control general. 
    Crear BBDD (crearbase.py) # Este módulo se encarga de las funciones de conexión y estructura de base de datos.
    Interfaz (interfaz.py, main.py) # Estos módulos son el punto de inicio y el armazón visual de la aplicación del proyecto.