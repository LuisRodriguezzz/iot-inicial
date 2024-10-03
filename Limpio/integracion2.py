from torSuscriber import suscriber
from datetime import datetime
import time
import pandas as pd
import requests

#Función para enviar una notificación (ejemplo con Telegram)
def enviar_notificacion(notificacion):
    token = "7505196905:AAFrQhr9A3R4aqfDMhuGSzQWM7dVbP7ZXmo"  # Reemplaza con tu token de Telegram
    chat_id = "1732985833"  # Reemplaza con tu chat ID de Telegram
    mensaje = f"Alerta: El PE {notificacion} " # Mensaje de la notificación
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensaje}"
    requests.get(url)

obtener_datos = suscriber('test/topic')
