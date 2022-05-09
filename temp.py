import Adafruit_DHT
import os
import time
import paho.mqtt.client as paho
from MQTTClient import on_connect, on_message, on_publish, on_subscribe, getserial
from dotenv import load_dotenv

load_dotenv()

DHT_SENSOR  = Adafruit_DHT.DHT11

DHT_PIN = int(os.environ['DHT_PIN'])
usr = os.environ['USRDHT']
psw = os.environ['PSW']
device = getserial()
hostname = os.environ['HOSTNAME']
top = "device/"+str(device)+"/dht"


humidity    = None
temperature = None


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
client.connect(hostname, 8883)
client.loop_start()
while not client.connected_flag: #wait in loop
    print("In wait loop 1, connection DHT")
    time.sleep(1)
client.loop_stop() 

#publishing loop

while True: 
    client.loop_start()
    
    time.sleep(1)
    client.published_flag = False  
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None or temperature is not None:
        while not client.published_flag:
            print("H:"+str(int(humidity))+",T:"+str(int(temperature)))
            client.publish(top,"H:"+str(int(humidity))+",T:"+str(int(temperature)) , 0)
            print("In wait loop2, reading DHT")
            time.sleep(1)
        
    client.loop_stop() 
