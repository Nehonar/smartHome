import pytest
from time import sleep

from smarthome.communication.mqtt_client import MQTTClient

# Configuración básica del cliente MQTT para testing
BROKER_ADDRESS = "test.mosquitto.org"
PORT = 1883
TOPIC = "smarthome/testing"

@pytest.fixture
def mqtt_client():
    """
    Fixture to create a MQTT client for testing.
    """
    client = MQTTClient()
    client.connect(BROKER_ADDRESS, PORT)
    yield client
    client.disconnect()

def test_mqtt_connection(mqtt_client):
    """
    Test to verify the MQTT connection.
    """
    mqtt_client.loop_start()
    sleep(2) # Esperar para asegurar que la conexión se establezca
    assert mqtt_client.is_connected() == True
    mqtt_client.loop_stop()

def test_publish_message(mqtt_client):
    """
    Test to verify the publishing of a message to a topic.
    """
    message = "Hello, SmartHome!"
    mqtt_client.loop_start()
    mqtt_client.publish(TOPIC, message)
    sleep(2) # Esperar para asegurar que el mensaje se envíe
    # Aquí deberías tener alguna forma de verificar que el mensaje fue recibido/enviado correctamente.
    # Esto podría ser un callback a otro cliente de prueba suscrito al mismo tópico, por ejemplo.
    mqtt_client.loop_stop()

def test_subscribe_to_topic(mqtt_client):
    """
    Test to verify the subscription to a topic.
    """
    global received_message
    received_message = None
    
    mqtt_client.loop_start()
    mqtt_client.subscribe(TOPIC)
    mqtt_client.publish(TOPIC, "Test message")
    
    sleep(2)
    
    assert received_message == "Test message"
    mqtt_client.loop_stop()
