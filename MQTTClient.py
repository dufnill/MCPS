import paho.mqtt.client as paho


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code= ",rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    if mid is not None:
        client.published_flag=True #set flag
        print("Published " +str(mid))
    else:
        print("Not published")


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    """
        Prints a reassurance for successfully subscribing
        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
        :param granted_qos: this is the qos that you declare when subscribing, use the same one for publishing
        :param properties: can be used in MQTTv5, but is optional
    """
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):

    if str(msg.payload[0]) == '0':
        gp.output(client.REDPIN, False)
    else:
        gp.output(client.REDPIN, True)
    if str(msg.payload[1]) == '0':
        gp.output(client.BLUEPIN, False)
    else:
        gp.output(client.BLUEPIN, True)

    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
