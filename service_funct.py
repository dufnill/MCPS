from MQTTClient import MQTTClient


def subscribe_to_topic(sub: MQTTClient, usr: str, psw: str, con_str: str, port: int, topic: str, qos: int):
    
    sub.connect(usr, psw, con_str, port)
    sub.subscribe(topic, qos)
    