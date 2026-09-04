import time
from wifi import connect_wifi
from machine import Pin
from dht import DHT11
from umqtt.simple import MQTTClient
import json
time.sleep(0.1)

TOPIC = b"home/pico/dht11"
MQTT_BROKER = "10.54.4.148"
status_led = Pin(15, 1)

dht_sensor = DHT11(Pin(16))


print(connect_wifi())

if connect_wifi():
    status_led.value(1)

def connect_mqtt():
    client = MQTTClient(client_id="pico", server=MQTT_BROKER, port=1883)
    client.connect()
    print("connec to mqtt")
    return client

client = connect_mqtt()

while True:
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    data = {"temprature": temp, "humidity": humidity}
    print(data)


    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    time.sleep(1)