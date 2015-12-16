import OSC
import time, sys
import time, random

client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57110 ) )

def oscgrain( frequency, vol, sustain ):
    msg = OSC.OSCMessage()
    msg.setAddress("s_new")
    msg.append("grain")
    msg.append(-1)
    msg.append(0)
    msg.append(1)
    msg.append("amp")
    msg.append(vol)
    msg.append("freq")
    msg.append(frequency)     #read in data points
    msg.append("sustain")
    msg.append(sustain)
    client.send(msg)

oscgrain(5000, 0.8, 0.1)
