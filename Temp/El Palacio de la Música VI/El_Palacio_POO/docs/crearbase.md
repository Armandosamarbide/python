# Configuración de la Base de Datos (crearbase.py)

Este módulo se encarga de las funciones de conexión y estructura de base de datos.

No hay interacción del usuario final con este módulo.

## Conexión

Establece la comunicación entre la aplicación y la base de datos MySQL.

La aplicación intenta conectarse automáticamente con la base de datos llamada discos en la ubicación local (localhost) usando las credenciales predeterminadas de administrador (user="root", passwd="").

## Creación de la Estructura Tabla

Verifica si la tabla donde se guardan los discos (listadiscos) ya existe; si no, la crea automáticamente. Los campos de la tabla son:

- Un ID único (para que la aplicación pueda identificar cada disco);
- Título;
- Artista;
- Año;
- Género.

Esta función asegura que la estructura de la base de datos esté lista para que el usuario pueda empezar a añadir discos de inmediato.