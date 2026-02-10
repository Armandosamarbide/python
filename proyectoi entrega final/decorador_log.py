from __future__ import annotations

from datetime import datetime
from functools import wraps
import os


LOG_FILENAME = "app.log"


def _safe_repr(value, max_len: int = 120) -> str:
    try:
        s = repr(value)
    except Exception:
        s = "<unreprable>"
    if len(s) > max_len:
        return s[: max_len - 3] + "..."
    return s


def _write_line(line: str) -> None:
    ruta = os.path.join(os.path.dirname(__file__), LOG_FILENAME)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def log_accion(nombre: str | None = None):
    def decorator(func):
        accion = nombre or func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            args_s = [_safe_repr(a) for a in (args[1:] if len(args) > 0 else [])]
            kwargs_s = {k: _safe_repr(v) for k, v in kwargs.items()}

            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            _write_line(f"[{ts}] CALL {accion} args={args_s} kwargs={kwargs_s}")

            resultado = func(*args, **kwargs)

            ts2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            extra = ""
            if isinstance(resultado, dict) and "completado" in resultado:
                extra = f" completado={resultado.get('completado')}"
            _write_line(f"[{ts2}] END  {accion}{extra}")
            return resultado

        return wrapper

    return decorator
