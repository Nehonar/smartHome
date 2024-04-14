import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port=1883):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
