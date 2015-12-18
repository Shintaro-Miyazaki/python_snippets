# example
import sys
import random
import time
import os
import fcntl
import pysimpledmx

mydmx = pysimpledmx.DMXConnection(3)
mydmx.setChannel(401, 255) # set DMX channel 1 to full
