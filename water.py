#import RPi.GPIO as gp
import time

from MQTTClient import on_connect, on_message, on_publish, on_subscribe
import paho.mqtt.client as paho

"""HYG_PIN = 8
water = None

gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(HYG_PIN, gp.IN)"""

usr = "hygsensor"
psw  = "Password1"
top = "plant/water"
port = 8883
hostname = '40aa8266336d412198db9594ff2f47ed.s1.eu.hivemq.cloud'

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
    time.sleep(10)
    client.published_flag = False  
    humidity, temperature = "20"
    """
    while humidity is not None and temperature is not None:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    """
    while not client.published_flag:
        client.publish(top,"H:"+str(humidity)+",T:"+str(temperature) , 1)
        print("In wait loop2, reading HYGROMETER")
        time.sleep(1)
    client.loop_stop() 



