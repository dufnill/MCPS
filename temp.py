#import Adafruit_DHT
import os
import time
import paho.mqtt.client as paho
from MQTTClient import on_connect, on_message, on_publish, on_subscribe

#DHT_SENSOR  = Adafruit_DHT.DHT11
DHT_PIN     = 4

humidity    = None
temperature = None

usr = "dhtsensor"
psw = "Password1"
conn = "connection_string"
toph = "plant/humidity"
topt = "plant/temperature"
hostname = '40aa8266336d412198db9594ff2f47ed.s1.eu.hivemq.cloud'

#new instance of a client
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
    print("In wait loop1")
    time.sleep(1)
client.loop_stop() 

#publishing loop

while True: #wait in loop
    client.loop_start()
    time.sleep(10)
    client.published_flag = False   
    while not client.published_flag:
        client.publish('home', '00', 1)
        print("In wait loop1")
        time.sleep(1)
    client.loop_stop() 