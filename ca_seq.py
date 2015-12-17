import sys
import random
import time
import os
import fcntl
import random
# import pyfirmata

# Arduino-Pyfirmata CODE

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
# PORT = '/dev/ttyACM0'

# Creates a new board
# board = pyfirmata.Arduino(PORT)

# Celluar Automata section


def makecells(rule, iterations):
    WIDTH=20               # How wide is the pattern?
    w = WIDTH * [0]         # create the current generation
    nw = WIDTH * [0]        # and the next generation
    w[WIDTH/2] = 1          # populate with a single one
    NEIGHBORHOOD=3
    rtab = (2**NEIGHBORHOOD) * [0]
    
    for i in range(2**NEIGHBORHOOD):
        if ((2**i) & rule) != 0:
            rtab[i] = 1

    def dump(r):
        for x in r:
            if x == 1:
                sys.stdout.write('X')
            else:
                sys.stdout.write(' ')
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
        time.sleep(0.01)

makecells(30, 100)
makecells(90, 100)
