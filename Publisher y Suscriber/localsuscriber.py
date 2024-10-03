import paho.mqtt.client as mqtt

# Configuración del broker MQTT
broker = 'localhost'  # Usar 'localhost' ya que Mosquitto está instalado localmente
port = 1883           # Puerto estándar para MQTT sin TLS
topic = 'test/topic'  # El topic al que se suscribirá

# Función de callback cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en el topic {message.topic}: {message.payload.decode()}")

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_message = on_message  # Asignar la función de callback

# Conectar al broker
client.connect(broker, port)

# Suscribirse al topic
client.subscribe(topic)

# Iniciar bucle para recibir mensajes
client.loop_forever()
