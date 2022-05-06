from MQTTClient import MQTTClient

def send_a_sample_to_topic(client: MQTTClient, usr: str, psw: str, con_str: str, port: int, topic: str, message: str):
    
    client.connect(usr, psw, con_str, port, False)
    client.publish(topic, message)
    client.disconnect()

def subscribe_to_topic(sub: MQTTClient, usr: str, psw: str, con_str: str, port: int, topic: str, qos: int):
    
    sub.connect(usr, psw, con_str, port, False)
    sub.subscribe(topic, qos)
    