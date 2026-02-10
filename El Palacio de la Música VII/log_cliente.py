import socket

def enviar_log(mensaje, host='127.0.0.1', port=5000):
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(mensaje.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        
        ## Si el servidor de registros no funciona, lo ignoramos para que la aplicación pueda seguir funcionando sin problemas
        print(f"No se pudo enviar el log al servidor: {e}")
