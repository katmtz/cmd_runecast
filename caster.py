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
import random
from Rune import *

def hashToRune(hash, runebag):
    random.seed(hash)
    return random.choice(runebag)

def getRunes(topic, timeHash, runebag):
    upperHash = hash(topic.upper())
    lowerHash = hash(topic.lower())
    upperSeed = (upperHash ^ timeHash) + upperHash
    lowerSeed = (lowerHash ^ timeHash) + lowerHash
    upper = hashToRune(upperSeed, runebag)
    lower = hashToRune(lowerSeed, runebag)
    while (lower == upper):
        lower = hashToRune(lowerSeed, runebag)
    return (upper, lower)

def run(runebag):
    print("> CMD_FUTHARK \n ... \n ...")
    topicString = raw_input("> What would you like to know about?  ")
    timeStr = str(time.time())
    timeHash = hash(timeStr)
    (primary, secondary) = getRunes(topicString, timeHash, runebag);
    primary.printPrimary()
    secondary.printSecondary()
    ans = raw_input("> Press any key to continue... ")
    if (ans.lower() == 'quit'):
        sys.exit()
    return

if __name__ ==  '__main__':

    runenames = Rune.FUTHARK_LIST
    runebag = []
    for i in xrange(len(runenames)):
        runebag.insert(i, Futhark(runenames[i]))

    while(True):
        run(runebag)


