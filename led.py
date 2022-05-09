from MQTTClient import on_connect, on_message, on_publish, on_subscribe, getserial
from dotenv import load_dotenv

import RPi.GPIO as gp
import paho.mqtt.client as paho
import RPi.GPIO as gp
import time
import sys
import os

from dotenv import load_dotenv

load_dotenv()

BLUE_PIN= int(os.environ['BLUE_PIN'])
RED_PIN = int(os.environ['RED_PIN'])
usr = os.environ['USRLED']
psw  = os.environ['PSW']
device = getserial()
hostname = os.environ['HOSTNAME']
top = "device/"+str(device)+"/led"

gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(RED_PIN, gp.OUT)
gp.setup(BLUE_PIN, gp.OUT)
gp.output(RED_PIN, False)
gp.output(BLUE_PIN, False)

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
client.connect(hostname, 8883)
client.loop_start()
while not client.connected_flag: #wait in loop
    print("In wait loop, connecting leds")
    time.sleep(1)
client.loop_stop() 

#subscribing loop
client.loop_start()
client.subscribe(top,0)
time.sleep(3)
client.loop_stop() 

if client.on_subscribe:
    while True:
        try:
            client.loop()
            time.sleep(1)
        except KeyboardInterrupt:
            gp.output(client.BLUEPIN, False)
            gp.output(client.REDPIN, False)
            sys.exit()
