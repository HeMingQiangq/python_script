DEBUG = True


def VERBOSE(logstr):
    if DEBUG:
        print "[	VERBOSE	]: ---" + logstr + "---"


def INFO(logstr):
    if DEBUG:
        print "[	INFO	]: ---" + logstr + "---"


def INFO(arr):
    if DEBUG:
        print "[	INFO	]: ---"
        print arr
        print "---"


def WARNING(logstr):
    if DEBUG:
        print "[	WARNING	]: +++" + logstr + "+++"


def ERROR(logstr):
    if DEBUG:
        print "[	ERROR	]: ###" + logstr + "###"
