# Módulo Inicial e Interfaz Principal (main.py, interfaz.py)

Estos módulos son el punto de inicio y el armazón visual de la aplicación del proyecto.

## Módulo Inicial
Su única función es iniciar la aplicación.

Importa la clase principal InterfazApp. Cuando el archivo se ejecuta directamente, crea una instancia de InterfazApp.

Llama al método app.run(), que pone en marcha la interfaz gráfica.

## Módulo de Interfaz Principal (InterfazApp)

Es la parte de la aplicación que conecta todas las funcionalidades.

Al iniciar la aplicación, se realizan las siguientes configuraciones esenciales:

### Creación de la Ventana (self.root): 

Se crea la ventana principal de la aplicación, asignándole el título "Disquería EL PALACIO DE LA MÚSICA - POO Edition" y un tamaño inicial de 800x600 píxeles.

### Estructura Visual: Se divide la ventana en dos secciones principales:

Panel lateral izquierdo de color verde oscuro, dedicado a los botones de navegación.

Un área de texto que ocupa la mayor parte de la interfaz gráfica, utilizada para mostrar mensajes de éxito, errores o resultados de búsquedas/listados.

Asimismo, se invoca a BBDD.crear_tabla() para asegurar que la BBDD esté lista para que el usuario interactúe.

Se crea el menú lateral con botones que activan las distintas funcionalidades:

- Nuevo: muestra el formulario para crear un nuevo disco y grabarlo en la BBDD:
- Borrar: muestra el formulario para buscar y elimilar un disco de la BBDD.
- Modificar: muestra el formulario para buscar y editar los datos de un disco.
- Buscar: muestra el formulario para buscar discos por título o artista.
- Mostrar todo: muestra la lista completa de todos los discos en el área de mensajes.
- Limpiar pantalla: Borra todos los mensajes y el contenido del área central.
- Quit: se utiliza para salir de la aplicación. Alternativamente, se puede cerrar la ventana.