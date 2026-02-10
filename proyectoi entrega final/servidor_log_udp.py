import socketserver
from datetime import datetime
import os

HOST = "127.0.0.1"
PORT = 9999
LOG_FILENAME = "server.log"

def _write_server_log(linea: str) -> None:
    ruta = os.path.join(os.path.dirname(__file__), LOG_FILENAME)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(linea + "\n")

class LogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        sock = self.request[1]

        try:
            mensaje = data.decode("utf-8", errors="replace")
        except Exception:
            mensaje = str(data)

        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{ts}] {self.client_address[0]}:{self.client_address[1]} {mensaje}"
        _write_server_log(linea)

        try:
            sock.sendto(bytes([0xA0]), self.client_address)
        except Exception:
            pass

if __name__ == "__main__":
    with socketserver.UDPServer((HOST, PORT), LogUDPHandler) as server:
        print(f"Servidor UDP de logs escuchando en {HOST}:{PORT}")
        print("Se guardará en server.log (en la carpeta del proyecto).")
        server.serve_forever()
