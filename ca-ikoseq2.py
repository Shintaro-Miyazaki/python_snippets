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

def makecells(rule, iterations, unittime):

    # Celluar Automata section
    WIDTH=18               # How wide is the pattern?
    w = WIDTH * [0]         # create the current generation
    nw = WIDTH * [0]        # and the next generation
    w[WIDTH/2] = 1          # populate with a single one
    NEIGHBORHOOD=3
    rtab = (2**NEIGHBORHOOD) * [0]
    rulerule = rule

    for i in range(2**NEIGHBORHOOD):
        if ((2**i) & rulerule) != 0:
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

    for y in range(iterations):
        dump(w)
        for x in range(WIDTH):
            sum = 0
            for d in range(NEIGHBORHOOD):
                sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
            nw[x] = rtab[sum]
        w, nw = nw, w
# time control
        time.sleep(unittime)
        try:
            stdin = sys.stdin.read()
            if "\n" in stdin or "\r" in stdin:
                break
        except IOError:
            pass



makecells(30, 500, 0.1)
makecells(90, 500, 0.05)
makecells(105, 500, 0.02)
makecells(170, 500, 0.06)
