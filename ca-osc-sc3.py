import sys
import random
import time
import os
import fcntl
import random
import OSC

# implementation of Wolfram's 1D cellular automata
# https://en.wikipedia.org/wiki/Elementary_cellular_automaton
# http://plato.stanford.edu/entries/cellular-automata/supplement.html 

# setup OSC client and connecting with supercollider
c = OSC.OSCClient()
c.connect( ( '127.0.0.1', 57110 ) )

# How wide is the pattern?
WIDTH = int(sys.argv[2])
# create the current generation => array
w = WIDTH * [0]

# and the next generation
nw = WIDTH * [0]

# populate with a single one in the middle of the array
w[WIDTH/2] = 1

# or alternatively, you can populate it with a random
# initial configuration.  If you want to start with
# just a single one, comment the next two lines out.

# for i in range(WIDTH):
#      w[i] = random.randint(0, 1)

# Setting neighborhood
# How wide is the neighborhood of cells that are
# examined? The traditional Wolfram 1D cellular
# automata uses a neighborhood of 3...
NEIGHBORHOOD=3
# There are 8 (2**3) possible configurations for a cell
# and its two immediate neighbors for 1D-CAs.
# 111 110 101 100 011 010 001 000
# The rule defining the cellular automaton must
# specify the resulting state for each of these
# possibilities so there are 256 possible
# elementary cellular automata.
# 0 1 1 0 1 1 1 0 => rule 110
# so for example if you have 111 as a configuration
# then the next generation at this position
# will be a 0 when rule 110 is acquired.
# if you have the neighborhood-pattern 110 then 1.

# rtab is a space for the rule table.  It maps all
# numbers from [0, 2**NEIGHBORHOOD) to either a 0 or 1. (** = exponential)
rtab = (2**NEIGHBORHOOD) * [0]
# rtab = 8 * [0]
# [0] = array with one element.
# Multipling it with 8 makes an array with 8 zeros.
# rtab = [0, 0, 0, 0, 0, 0, 0, 0]

# The "rule" is a number which is used to populate
# rtab. The number is in the range [0, 2**(2**NEIGHBORHOOD))
# 2**8 = 256
# Many rules generate uninteresting patterns, but some
# like 30 generate interesting, aperiodic patterns.
rule = int(sys.argv[1])

# This fills in the table with ones
# according to the rule pattern
# but backwards/ reversed => read-in from the least significant bit
for i in range(2**NEIGHBORHOOD):
    if ((2**i) & rule) != 0:
        rtab[i] = 1
# range 8 = i in [0, 1, 2, 3, 4, 5, 6, 7] => for loop will repeat 8 times
# & returns the result of bitwise AND of two integers

# For example with i = 2 and rule 110
# 2**i => 2**2= 4
# rule = 110 => 01101110
# 01101110 => decimal 110
# 00000100 => decimal 4
# 00000100 => decimal 4
# if result is not equal 0
# then set rtab at position i (for example 2) as 1
# now rtab = [0, 0, 1, 0, 0, 0, 0, 0]

# the loop create at the end:
# rtab = [0,1,1,1,0,1,1,0]
# rule = 110 => 01101110

# function to create print-out in terminal
# needs to get defined before next for loop
def dump(r):
    for x in r:
        if x == 1:
            sys.stdout.write('X')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

# Speed and number of lines for next for loop
# For loop generates lines
speed = float(sys.argv[3]) # speed = seconds for example 0.01
numlines = int(sys.argv[4]) # number of "lines" for example 100

# Sending OSC
def playclick(panval):
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
    msg.append(panval)
    c.send(msg)

# This generates the lines and generations
for y in range(numlines):
    dump(w) #dump array of current generation (w) to terminal
    # then do a for loop: x in [0, 1, 2 ...WIDTH-1]
    for x in range(WIDTH):
        sum = 0
        # d in [0, 1, 2]
        # sum = sum + (2**d) * w[(x+d+8 - 3/2) % WIDTH]
        # 0 = 0 + 2 * w[]
        # index = ([0,1,2.. 19]+[0,1,2]+8 - 3/2) % 20
        # index = 6.5 % 20 = 0.325
        # % modulus
        # divides left hand operand by right hand operand and returns remainder
        for d in range(NEIGHBORHOOD):
            sum = sum + (2**d) * w[(x+d+WIDTH - NEIGHBORHOOD/2) % WIDTH]
        nw[x] = rtab[sum]
    w, nw = nw, w #swapping
# time control
    playclick(1.0)
    # value needs to be between -1.0 and 1.0 this needs to get
    # "mapped" to array w or nw with size WIDTH
    # check index/position in array map  and whether 1 or 0.
    time.sleep(speed)
