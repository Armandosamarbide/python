import os
import socket
from datetime import datetime


class Observador:
    def update(self, evento, data):
        raise NotImplementedError("Subclases deben implementar update()")


class Observable:
    def __init__(self):
        self._observadores = []

    def attach(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def detach(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notify(self, evento, data=None, **kwargs):
        if data is None:
            data = {}
        if isinstance(data, dict):
            data.update(kwargs)
        else:
            data = {"data": data, **kwargs}

        for obs in list(self._observadores):
            try:
                obs.update(evento, data)
            except Exception:
                pass


class LogObserver(Observador):
    def __init__(self, log_file="app.log", server_host="127.0.0.1", server_port=9999, timeout=0.5):
        self.log_file = log_file
        self.server_host = server_host
        self.server_port = server_port
        self.timeout = timeout

    def _log_path(self):
        return os.path.join(os.path.dirname(__file__), self.log_file)

    def update(self, evento, data=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} | OBSERVER | {evento} | {data}\n"

        try:
            with open(self._log_path(), "a", encoding="utf-8") as f:
                f.write(line)
        except Exception:
            pass

        try:
            msg = f"{timestamp} | {evento} | {data}"
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)
            sock.sendto(msg.encode("utf-8"), (self.server_host, self.server_port))

            try:
                sock.recvfrom(1024)
            except Exception:
                pass
            finally:
                try:
                    sock.close()
                except Exception:
                    pass
        except Exception:
            pass
