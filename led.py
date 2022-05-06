

import RPi.GPIO as gp
from service_funct import subscribe_to_topic
from MQTTClient import MQTTClient

client  = MQTTClient("LED")

user = "led"
psw  = "password"
conn = "connection_string"
topl = "/plant/led"

subscribe_to_topic(client, user, psw, conn, topl, 1)
