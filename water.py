import RPi.GPIO as gp
from MQTTClient import MQTTClient
from service_funct import send_a_sample_to_topic
import time
from MQTTClient.temperature import send_a_sample_to_topic

HYG_PIN = 8
water = None

gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(HYG_PIN, gp.IN)

client = MQTTClient("HYG")

user = "hyg"
psw  = "password"
conn = "connection_string"
topw = "/plant/water"
port = 8883

while True:
    
    while water is None:
        water = not gp.input(HYG_PIN)
        
    send_a_sample_to_topic(client, user, psw, conn, port, topw, str(water))

    water = None

    time.sleep(60)



