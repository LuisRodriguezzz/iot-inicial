import paho.mqtt.publish as publish
import ssl
import paho.mqtt.client as mqtt  # Importar para definir el protocolo MQTT

# Configuración del broker
broker = 'd8335173442b4cd6bc71dfd3578fe5c2.s1.eu.hivemq.cloud'
port = 8883
username = 'hivemq.webclient.1724899402353'
password = 'BPaM0NAZ253bdhcf<.;:'

# Configuración de SSL/TLS
sslSettings = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
sslSettings.check_hostname = False
sslSettings.verify_mode = ssl.CERT_NONE

# Función para publicar un mensaje
def publish_message(topic, payload):
    try:
        publish.single(
            topic,
            payload,
            hostname=broker,
            port=port,
            auth={'username': username, 'password': password},
            tls=sslSettings,
            protocol=mqtt.MQTTv5  # Usar mqtt.MQTTv5 para especificar el protocolo
        )
        print("Mensaje publicado correctamente!")
    except Exception as e:
        print(f"Error al publicar el mensaje: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    publish_message('encyclopedia/temperature', 'GOD IS GOOD')
