import sys
import random
import time
import os
import fcntl
import random

WIDTH = 40              # How wide is the pattern?
w = WIDTH * [0]         # create the current generation
nw = WIDTH * [0]        # and the next generation
w[WIDTH/2] = 1          # populate with a single one

# How wide is the neighborhood of cells that are
# examined?  The traditional Wolfram 1D cellular
# automata uses a neighborhood of 3...
NEIGHBORHOOD=3

# rtab is an array for the rule table.
rtab = (2**NEIGHBORHOOD) * [0]
rule = 30

# This fills-in rtab (rule table)
# by reverse-reading the binary representation of the rule number (dec)
# in case of rule = 110 => 01101110
# rtab will be [0,1,1,1,0,1,1,0] after this loop
for i in range(2**NEIGHBORHOOD):
    if ((2**i) & rule) != 0:
        rtab[i] = 1

# This produces new generations of w
for y in range(40):
    # this will dump the 1s in w as Xs into the terminal
    for x in w:
        if x == 1:
            sys.stdout.write('X')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')
    # this is the core code I don't really understand
    for x in range(WIDTH):
        sum = 0
        for d in range(NEIGHBORHOOD):
            sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
        nw[x] = rtab[sum]
    w, nw = nw, w
    # time control
    time.sleep(0.07)
