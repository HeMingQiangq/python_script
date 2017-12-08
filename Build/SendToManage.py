# -*- coding: utf-8 -*-
import shutil, os, sys, getopt
import Logger, Util, Const
import os


def isSendToManage():
    if IS_SENDTO_MANAGE == "true":
        addPackageToChannel()
    elif IS_CHANNEL_BUILD == "true":
        jobSuccess()



def jobSuccess():
    command = "curl -X POST "+Const.CHANNEL_HOST+"/jobSuccess.action"
    print command
    os.system(command)





def addPackageToChannel():
    command = "curl -X POST "+Const.CHANNEL_HOST+"/addJP.action?version="+VERSION+"&platform="+PLATFORM+"&buildType="+BUILD_TYPE+"&download_url="+DOWNLOAD_URL
    print command
    os.system(command)





# =================MAIN====================#
def doBuild():
    Logger.INFO("[======begin build...======]")
    print "IS_SENDTO_MANAGE"+IS_SENDTO_MANAGE
    print "DOWNLOAD_URL"+DOWNLOAD_URL
    print "PLATFORM"+PLATFORM
    print "VERSION"+VERSION
    print "IS_CHANNEL_BUILD"+IS_CHANNEL_BUILD
    print "BUILD_TYPE"+BUILD_TYPE
    isSendToManage()


argLen = len(sys.argv)
if (argLen < 6):
    Logger.ERROR('参数个数错误！')
    exit(1)
IS_SENDTO_MANAGE = sys.argv[1]
BUILD_TYPE = sys.argv[2]
VERSION  = sys.argv[3]
PLATFORM = sys.argv[4]
DOWNLOAD_URL = sys.argv[5]
IS_CHANNEL_BUILD = sys.argv[6]


doBuild()
