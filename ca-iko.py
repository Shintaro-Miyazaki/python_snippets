import sys
import random
import os
import fcntl
import time
import OSC
import pyfirmata
from pyfirmata import ArduinoMega

# Arduino-Pyfirmata CODE

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/tty.usbmodem1451'

# Creates a new board
board = pyfirmata.ArduinoMega(PORT)

# OSC sending
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 7700 ) )

# Break on pushing enter
fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)

# Celluar Automata section
WIDTH=18               # How wide is the pattern?
w = WIDTH * [0]         # create the current generation
nw = WIDTH * [0]        # and the next generation
w[WIDTH/2] = 1          # populate with a single one
NEIGHBORHOOD=3
rtab = (2**NEIGHBORHOOD) * [0]

# The "rule" is a number which is used to populate
# rtab.  The number is in the range [0, 2**(2**NEIGHBORHOOD))
# Many rules generate uninteresting patterns, but some
# like 30 generate interesting, aperiodic patterns.

# input from commandline as simple arguments like: ca-firmata.py 30
# for rule 30
rule = int(sys.argv[1])

# This fills in the table...
for i in range(2**NEIGHBORHOOD):
    if ((2**i) & rule) != 0:
        rtab[i] = 1

def dump(r):
    pin = 14
    for x in r:
        if x == 1:
            sys.stdout.write('X')
        else:
            sys.stdout.write(' ')
        board.digital[pin].write(1 if x else 0)
	pin += 1
    sys.stdout.write('\n')

# and generates 100 lines...

for y in range(int(sys.argv[2])):
    dump(w)
    for x in range(WIDTH):
        sum = 0
        for d in range(NEIGHBORHOOD):
            sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
        nw[x] = rtab[sum]
    w, nw = nw, w
# time control
    time.sleep(float(sys.argv[3]))
    try:
        stdin = sys.stdin.read()
        if "\n" in stdin or "\r" in stdin:
            break
    except IOError:
        pass
