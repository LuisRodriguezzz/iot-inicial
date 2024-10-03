import paho.mqtt.client as mqtt

# Configuración del broker MQTT
broker = 'localhost'  # Mosquitto corriendo localmente
port = 1883           # Puerto estándar para MQTT sin TLS
topic = 'test/topic'  # Topic al que se publicará el mensaje

# Función para publicar un mensaje
def publish_message(message):
    # Crear un cliente MQTT
    client = mqtt.Client()

    # Conectar al broker
    client.connect(broker, port)

    # Publicar el mensaje en el topic
    client.publish(topic, message)

    # Desconectar
    client.disconnect()

# Solicitar el mensaje al usuario y publicarlo
if __name__ == "__main__":
    mensaje = input("Escribe el mensaje a publicar: ")
    publish_message(mensaje)
    print("Mensaje publicado en el broker local.")
