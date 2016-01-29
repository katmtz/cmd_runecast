##
# > CMD_FUTHARK
# A simple, command-line run rune-casting program.
#
# Input a word or short phrase that sums up the thing
# you want to ask about. The phrase is used to set the
# RNG seed that selects a primary rune, and one clarifier.
# Your reading and a brief explanation of what your runes
# mean.
#
# Katherine Martinez
##
import sys
import time
from classes.Rune import *

def __main__(args):

    runenames = Rune.FUTHARK_LIST

    while(true):
        run()

def run():
    print("> CMD_FUTHARK \n ... \n ...")
    topicString = raw_input("> What would you like to know about?  ")
    timeHash = str(time.time()).hash()
    upperHash = topicString.uppercase().hash()
    lowerHash = topicString.lowercase().hash()
    primarySeed = (upperHash ^ timeHash) + upperHash
    secondarySeed = (lowerHash ^ timeHash) + lowerHash

