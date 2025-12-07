import paho.mqtt.client as mqtt
import time
import json

student_name = "Priyadharshini M D"
unique_id = "42111019"

topic = "home/priyadharshini-2025/sensor"

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

print("Publishing sensor data...")

while True:
    data = {
        "temperature": 25,
        "humidity": 60,
        "light": 300
    }

    client.publish(topic, json.dumps(data))
    print("Published:", data)

    time.sleep(5)
