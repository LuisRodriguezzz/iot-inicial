import paho.mqtt.client as paho
import ssl
import socks
import socket
import requests

#Función para enviar una notificación (ejemplo con Telegram)
def enviar_notificacion(notificacion):
    token = "7505196905:AAFrQhr9A3R4aqfDMhuGSzQWM7dVbP7ZXmo"  # Reemplaza con tu token de Telegram
    chat_id = "1732985833"  # Reemplaza con tu chat ID de Telegram
    mensaje = f"Alerta: {notificacion} " # Mensaje de la notificación
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensaje}"
    requests.get(url)

def suscriber(topic):
    # Configuración del proxy SOCKS5
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket
    mensaje = []

    # Callback que se llama cuando el cliente recibe un CONNACK del servidor
    def on_connect(client, userdata, flags, rc):
        print(f"Conectado con código de resultado {rc}")
        client.subscribe(topic, qos=1)

    # Callback que se llama cuando un mensaje ha sido recibido
    def on_message(client, userdata, msg):
        #print(f"Mensaje crudo recibido: {msg.payload}")
        try:
            payload_decoded = msg.payload.decode('utf-8')
            print(f"Mensaje decodificado: {payload_decoded}")
            enviar_notificacion(payload_decoded)
        except UnicodeDecodeError:
            print(f"Error al decodificar el mensaje del tema {msg.topic}")

    # Configuración del broker
    broker = 'd8335173442b4cd6bc71dfd3578fe5c2.s1.eu.hivemq.cloud'
    port = 8883
    username = 'hivemq.webclient.1724899402353'
    password = 'BPaM0NAZ253bdhcf<.;:'

    # Configuración de SSL/TLS
    sslSettings = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    sslSettings.check_hostname = False
    sslSettings.verify_mode = ssl.CERT_NONE

    # Crear cliente MQTT
    client = paho.Client()  
    client.on_connect = on_connect
    client.on_message = on_message

    # Configurar TLS y autenticación
    client.tls_set_context(sslSettings)
    client.username_pw_set(username, password)

    # Conectar al broker y comenzar el bucle de red
    client.connect(broker, port)
    client.loop_forever()

# Llamada de prueba
suscriber('test/topic') 
