import imp
import paho.mqtt.client as paho
#import RPi.GPIO as gp
import time
import os

from dotenv import load_dotenv
from MQTTClient import on_connect, on_message, on_subscribe, on_publish

load_dotenv()
HYG_PIN = 8
water = None
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(HYG_PIN, gp.IN)

usr = os.environ['USRHYG']
psw  = os.environ['PSW']
device = os.environ['DEVNAME']
hostname = os.environ['HOSTNAME']
top = "device/"+device+"/water"

client = paho.Client(client_id="", clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.connected_flag = False
client.published_flag = False
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
    print("In wait loop 1, connection HYGROMETER")
    time.sleep(1)
client.loop_stop() 

#publishing loop

while True: #wait in loop
    client.loop_start()
    time.sleep(1)
    client.published_flag = False 
    water = not gp.input(HYG_PIN)
    while not client.published_flag:
        print("W:"+str(int(water)))
        client.publish(top,"W:"+str(int(water)) , 0)
        print("In wait loop2, reading HYGROMETER")
        time.sleep(1)
    client.loop_stop() 
