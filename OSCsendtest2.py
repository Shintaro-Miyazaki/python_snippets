import OSC
import time, sys
import time, random

c = OSC.OSCClient()
c.connect( ( '127.0.0.1', 57110 ))

i = 0
while (i < 10):
    msg = OSC.OSCMessage()
    msg.setAddress("s_new")
    msg.append("grain")
    msg.append(-1)
    msg.append(0)
    msg.append(1)
    msg.append("freq")
    msg.append(20)
    msg.append("sustain")
    msg.append(0.001)
    msg.append("pan")
    msg.append(0.0)
    c.send(msg)
    time.sleep(0.5)
    i = i + 1
