import paho.mqtt.client as paho
import RPi.GPIO as gp

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
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    action = str(msg.payload)
    if '1' in action:
        gp.output(client.REDPIN, True)
    elif '2' in action:
        gp.output(client.REDPIN, False)
    elif '3' in action:
        gp.output(client.BLUEPIN, True)
    elif '4' in action:
        gp.output(client.BLUEPIN, False)

    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
          if line[0:6]=='Serial':
            cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    return cpuserial
