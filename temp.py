import Adafruit_DHT
from MQTTClient import MQTTClient
from service_funct import send_a_sample_to_topic
import time

from MQTTClient.temperature import send_a_sample_to_topic

DHT_SENSOR  = Adafruit_DHT.DHT11
DHT_PIN     = 4

humidity    = None
temperature = None

client  = MQTTClient("DHT")

user = "dht"
psw  = "password"
conn = "connection_string"
toph = "/plant/humidity"
topt = "/plant/temperature"
port1 = 8883
port2 = 8883

while True:
    
    while humidity is not None and temperature is not None:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    send_a_sample_to_topic(client, user, psw, conn, port1, toph, str(humidity))
    send_a_sample_to_topic(client, user, psw, conn, port2, topt, str(temperature))

    humidity    = None
    temperature = None

    time.sleep(60)



