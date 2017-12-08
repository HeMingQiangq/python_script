#!/usr/bin/env Python  
# coding=utf-8
import sys, string
import os, shutil

oldPkg = "com.rrh.jdb"
newPkg = sys.argv[1]
basePath = sys.argv[2]

if oldPkg == newPkg:
    exit(0)

projects = ["JDB"]
handleWhtlist = ["com.rrh.jdb.common.lib.util.CompatibleUtils"]
blkStringList = []
fileSuffix = ["jpg", "png", "apk", "so", "jar", "mk", "exe"]


def main():
    print ("********************Now rename the packageName!************************")
    for project in projects:
        handleDir(basePath + os.sep + project + os.sep)


def handleDir(fileDir):
    if not os.path.exists(fileDir):
        print ("[Convert PackageName Warning] dir: " + fileDir + " does not exists!")
        return
    fileList = os.listdir(fileDir)
    for tmpStr in fileList:
        fileStr = fileDir + tmpStr
        if os.path.isfile(fileStr):
            handleFile(fileStr)
        elif os.path.isdir(fileStr) and fileStr.find(".svn") == -1:
            handleDir(fileStr + os.sep)
    if fileDir.strip(os.sep).endswith(os.sep.join(oldPkg.split('.'))):
        destDir = fileDir.replace(os.sep.join(oldPkg.split('.')), os.sep.join(newPkg.split('.')))
        print("[Convert PackageName] move from: " + fileDir + " to : " + destDir)
        shutil.move(fileDir, destDir)


def handleFile(fileStr, oldName=oldPkg, newName=newPkg):
    if not os.path.exists(fileStr):
        print ("[Convert PackageName Warning] file: " + fileStr + " does not exists!")
        return
    if not isTextFile(fileStr):
        return
    print ("[Convert PackageName] " + fileStr)
    file = open(fileStr, 'r')
    contentList = file.readlines()
    file.close()
    objList = []
    file = open(fileStr, 'w')
    line = 0
    for contentStr in contentList:
        line += 1
        for blkStr in blkStringList:
            if contentStr.find(blkStr) != -1:
                objList.append("//Bad string error:" + contentStr)
                print('[Bad string error]:Find bad string "' + blkStr + '",in line:' + line + ' "' + contentStr + '"!')
                break
        for whtStr in handleWhtlist:
            if contentStr.find(whtStr) != -1:
                objList.append(contentStr)
                break
        else:
            objList.append(contentStr.replace(oldName, newName, contentStr.count(oldName)))

    file.writelines(objList)
    file.close()


def isTextFile1(fileStr):
    for str in fileSuffix:
        if os.path.basename(fileStr).endswith(str):
            return False
    else:
        if os.path.basename(fileStr).find(".") == -1:
            return False
        else:
            return True


def isTextFile(filename, blocksize=512):
    file = open(filename)
    str = file.read(blocksize)
    file.close()
    if "\0" in str:
        return False
    return isTextFile1(filename)


if __name__ == '__main__':
    main()
