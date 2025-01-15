import random
import time
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(50.0, 60.0)
    payload = f"temperature:{temperature},humidity:{humidity}"
    client.publish(topic, payload)
    print(f"Published: {payload}")
    time.sleep(5)
