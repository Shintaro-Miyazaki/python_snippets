import OSC
import time, sys
import time, random

c = OSC.OSCClient()
c.connect( ( '127.0.0.1', 7700 ) )


msg = OSC.OSCMessage("/0/dmx/402")
msg.append(255)
c.send(msg)
time.sleep(3)
msg = OSC.OSCMessage("/0/dmx/402")
msg.append(25)
c.send(msg)
