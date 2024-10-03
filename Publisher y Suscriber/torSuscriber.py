import paho.mqtt.client as paho
import ssl
import socks
import socket
import time

# Configuración del proxy SOCKS5
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

# Callback que se llama cuando el cliente recibe un CONNACK del servidor
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Conectado con código de resultado {rc}")
    # Suscribirse al tema "encyclopedia/#" cuando se establece la conexión
    client.subscribe("encyclopedia/#", qos=1)

# Callback que se llama cuando un mensaje ha sido recibido
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en tema {msg.topic}: {msg.payload.decode()}")

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
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

# Configurar TLS y autenticación
client.tls_set_context(sslSettings)
client.username_pw_set(username, password)

# Conectar al broker
client.connect(broker, port)

# Bucle para recibir mensajes cada 10 segundos
try:
    while True:
        client.loop()  # Procesar mensajes
        time.sleep(10)  # Esperar 10 segundos
except KeyboardInterrupt:
    print("Interrumpido por el usuario, cerrando...")
finally:
    client.disconnect()  # Desconectar del broker
