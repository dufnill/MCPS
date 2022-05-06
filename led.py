

#import RPi.GPIO as gp
from MQTTClient import on_connect, on_message, on_publish, on_subscribe
import paho.mqtt.client as paho
import time

from prova import BLUE_PIN, RED_PIN

"""
BLUE_PIN= 15
RED_PIN = 16
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(RED_PIN, gp.OUT)
gp.setup(BLUE_PIN, gp.OUT)
gp.output(RED_PIN, False)
gp.output(BLUE_PIN, False)
"""

usr = "ledactuator"
psw  = "Password1"
top = "plant/led"
hostname = '40aa8266336d412198db9594ff2f47ed.s1.eu.hivemq.cloud'

client = paho.Client(client_id="", clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.connected_flag = False
client.REDPIN = RED_PIN
client.BLUEPIN = BLUE_PIN

client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)

client.on_connect      = on_connect
client.on_subscribe    = on_subscribe
client.on_message      = on_message
client.on_publish      = on_publish
client.username_pw_set(usr, psw) 


#connection loop
client.loop_start()
client.connect(hostname, 8883)
while not client.connected_flag: #wait in loop
    print("In wait loop, connecting leds")
    time.sleep(1)
client.loop_stop() 

#subscribing loop

client.loop_start()
client.subscribe(top, 2)
time.sleep(3)
client.loop_stop()