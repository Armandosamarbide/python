## Este archivo es el código de un servidor que recibe mensajes de log y los guarda en un archivo.

import socket
import os

def start_server(host='127.0.0.1', port=5000):
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Servidor escuchando en {host}:{port}...")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Conexión desde {addr}")
            
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print(f"Log recibido: {data.strip()}")
                with open("log_remoto.txt", "a", encoding="utf-8") as f:
                    f.write(data)
            
            client_socket.close()
    except KeyboardInterrupt:
        print("\nEl servidor se ha detenido.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
