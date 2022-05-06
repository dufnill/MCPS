

import RPi.GPIO as gp
from service_funct import subscribe_to_topic
from MQTTClient import MQTTClient

BLUE_PIN = 15
RED_PIN  = 16

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(RED_PIN, gp.OUT)
gp.setup(BLUE_PIN, gp.OUT)

gp.output(RED_PIN, False)
gp.output(BLUE_PIN, False)

client  = MQTTClient("LED")

user = "led"
psw  = "password"
conn = "connection_string"
topl = "/plant/led"

subscribe_to_topic(client, user, psw, conn, topic, 1)
