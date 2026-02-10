## Este archivo envía mensajes de prueba al servidor.

from log_cliente import enviar_log
import time

print("Enviando logs de prueba...")
enviar_log("TEST: 123 probando! 1\n")
time.sleep(1)
enviar_log("TEST: Testing testing 2\n")
print("Logs de prueba enviados.")
