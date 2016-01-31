##
# Generic Rune Class - represents a rune
# of any set and any name. Dummy name and runeset.
#
# Futhark (Parent: Rune) - represents a futhark rune.
# initialized with a name in futhark list, and runeset as
# 'futhark' 
# Katherine Martinez
##
class Rune:

    # "static" list of futhark rune names
    FUTHARK_LIST = ['ansuz',
                         'algiz',
                         'fehu',
                         'uruz',
                         'thuriaz',
                         'raido',
                         'kaunan',
                         'gebo',
                         'wunjo',
                         'hagalaz',
                         'naudiz',
                         'isa',
                         'jera',
                         'eihwaz',
                         'perthro',
                         'sowilo',
                         'teiwaz',
                         'berkanan',
                         'ehwaz',
                         'mannaz',
                         'laguz',
                         'ingwaz',
                         'othala',
                         'dagaz'
                        ]

    def __init__(self):
        self.name = "DEFAULT"
        self.runeset = "DEFAULT"

    def getPath(self):
        return "text/" + self.runeset + "/" + self.name + "/"

    def getRuneset(self):
        return self.runeset

    def getName(self):
        return self.name

    def getPrimaryPath(self):
        return self.getPath() + "primary.txt"

    def getSecondaryPath(self):
        return self.getPath() + "secondary.txt"

    def printPrimary(self):
        textFile = open(self.getPrimaryPath())
        textMsg = textFile.read(255)
        print "< Primary Rune: \n< ", textMsg

    def printSecondary(self):
        textFile = open(self.getSecondaryPath())
        textMsg = textFile.read(255)
        print "< Clarified by: \n< ", textMsg

class Futhark(Rune):

    def __init__(self, name):
        self.runeset = "futhark"
        self.name = name
