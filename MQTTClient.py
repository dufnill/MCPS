import paho.mqtt.client as paho
import RPi.GPIO as gp
import time


class MQTTClient:

    def __init__(self, identifier: str):
        self.identifier = identifier
        self.client = paho.Client(client_id="", clean_session=True, userdata=None, protocol=paho.MQTTv31)
        self.client.on_connect = self.on_connect
        self.client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)

        if identifier == 'led':
            self.REDPIN = 15
            self.BLUEPIN = 16
            gp.setwarnings(False)
            gp.setmode(gp.BOARD)
            gp.setup(self.REDPIN, gp.OUT)
            gp.setup(self.BLUEPIN, gp.OUT)
            gp.output(self.RED_PIN, False)
            gp.output(self.BLUE_PIN, False)
        

    #SUBSCRIBERS METHODS
    #
    #
    def subscribe(self, topic: str, qos: int):
        if qos <= 2 and qos >= 0:
            # subscribe to the topic "my/test/topic"
            self.client.subscribe(topic, qos)  # client.unsubscribe("my/test/topic")
            # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
            self.client.loop_forever()

    def unsubscribe(self, topic: str):
        self.client.unsubscribe(topic)

    def on_message(self, client, userdata, msg):

        payload = msg.payload.decode("utf-8")

        
        if self.identifier == 'led' and msg.topic == '/plant/led': #handle leds
            if payload[0] == '0':
                gp.output(self.RED_PIN, False)
            else:
                gp.output(self.RED_PIN, True)
            
            if payload[1] == '0':
                gp.output(self.BLUEPIN, False)
            else:
                gp.output(self.BLUEPIN, True)

        print("Received message: " + msg.topic + " -> " + payload) #possible 
        self.disconnect()
    #
    #
    ##########################################

    #PUBLISHER METHODS
    #
    #
    def publish(self, topic: str, payload: str, qos):
        self.client.publish(topic, payload, qos=qos)
        time.sleep(1)
    #
    #
    ##########################################


    #CONNECTION METHODS
    #
    #
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc, prot):
        if rc == 0:
            print("Connected successfully")
        else:
            print("Connect returned result code: " + str(rc))

    def disconnect(self):
        self.client.disconnect()

    # The callback for when a PUBLISH message is received from the server.
    def connect(self, user: str, passwd: str, conn_str: str, port: int, clean_start=False):
        # set username and password
        self.client.username_pw_set(user, passwd)
        # connect to HiveMQ Cloud on port 8883
        self.client.connect(conn_str, port, clean_start=clean_start)
    #
    #
    ##########################################