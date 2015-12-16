import OSC
import time, sys
import time, random

client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 7700 ) )

def oscdmx(val):
    msg = OSC.OSCMessage()
    msg.setAddress("/0/dmx/402")
    msg.append(val)
    client.send(msg)

oscdmx(255)
time.sleep(10)
oscdmx(0)
