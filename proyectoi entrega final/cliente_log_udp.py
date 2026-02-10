import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999

def enviar(mensaje: str) -> bytes:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)
    try:
        sock.sendto(mensaje.encode("utf-8"), (SERVER_HOST, SERVER_PORT))
        try:
            data, _ = sock.recvfrom(1024)
            return data
        except (socket.timeout, ConnectionResetError, OSError) as e:
            # Si el servidor no está levantado o no responde, no rompemos
            print("No se recibió ACK (servidor apagado o bloqueado):", e)
            return b""
    finally:
        try:
            sock.close()
        except Exception:
            pass

if __name__ == "__main__":
    ack = enviar("Prueba de log desde cliente independiente")
    print("ACK recibido:", ack)
