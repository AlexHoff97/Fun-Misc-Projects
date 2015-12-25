import sys
import random
import os
from word import *

def printHangman(size):
    if size == 1:
        print " O "
    elif size == 2:
        print " O/"
    elif size == 3:
        print "\O/"
    elif size == 4:
        print "\O/"
        print " | "
    elif size == 5:
        print "\O/"
        print " | "
        print "/  "
    elif size == 6:
        print "\O/"
        print " | "
        print "/ \\"
    return

if __name__ == '__main__':
    word = WordGame()
