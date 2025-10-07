from flask import Flask, request, render_template, redirect, url_for, flash

# Flask: La clase principal de la aplicación web.
# request: Objeto que contiene los datos de la petición HTTP (incluyendo los datos del formulario).
# render_template: Para renderizar archivos HTML.
# redirect: Para redirigir al usuario a otra URL.
# url_for: Para generar URLs dinámicamente.
# flash: Para enviar mensajes temporales al usuario (necesita app.secret_key).

app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_y_segura' # Necesario para flash messages

# Flask necesita una clave secreta para gestionar sesiones y flash messages de forma segura. En un entorno de producción, 
# esta clave debe ser muy compleja y generada de forma segura (por ejemplo, con os.urandom(24)).

# Flask es un framework ligero

# Ruta para mostrar el formulario (GET)
@app.route('/')
def mostrar_formulario():
    # render_template busca el archivo index.html en la carpeta 'templates'
    # o en la misma carpeta del script si no hay 'templates'
    return render_template('index.html')

# Ruta para procesar el formulario (POST)
@app.route('/guardar-texto', methods=['POST'])
def guardar_texto():
    if request.method == 'POST':
        # Obtener el texto enviado desde el formulario
        texto_recibido = request.form['texto_input']
        
        nombre_archivo = 'texto_guardado.txt'
        
        try:
            # Abrir el archivo en modo append ('a') para añadir al final
            # 'utf-8' para manejar caracteres especiales correctamente
            with open(nombre_archivo, 'a', encoding='utf-8') as f:
                f.write(texto_recibido + '\n') # Añadir un salto de línea
            
            # Mensaje de éxito
            flash('Texto guardado exitosamente.', 'exito')
            
        except Exception as e:
            # Mensaje de error
            flash(f'Ocurrió un error al guardar el texto: {e}', 'error')
            
        # Redirigir al usuario de vuelta al formulario después de guardar
        # Esto previene que el formulario se envíe de nuevo si el usuario recarga
        return redirect(url_for('mostrar_formulario'))

if __name__ == '__main__':
    # Ejecutar la aplicación Flask en modo depuración (útil para desarrollo)
    app.run(debug=True)