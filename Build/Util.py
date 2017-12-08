# -*- coding: utf-8 -*-
import os, Logger, shutil, hashlib, time, subprocess
import platform, re
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def ExecCmd(cmd):
    Logger.INFO(cmd)
    ret = os.popen(cmd)
    print ret.read()


def ExecCmdWithSubProc(cmd):
    Logger.INFO(cmd)
    ret = subprocess.check_call(cmd, shell=True)
    print ret


def ExecCmdWithSubProcParallel(cmd):
    Logger.INFO(cmd)
    ret = subprocess.Popen(cmd, shell=True)
    print ret
    return ret


def copyFile(srcFile, destFolder):
    try:
        Logger.INFO("copy File: " + srcFile + " to " + destFolder)
        shutil.copy(srcFile, destFolder)
    except Exception as ex:
        Logger.ERROR("Copy File failed:")
        print ex
        exit(1)


def CopyFolder(srcFolder, destFolder):
    Logger.INFO("Copying file from :" + srcFolder + " to: " + destFolder)
    '''
    Add copy folder code for different platform
    '''
    if platform.system() == "Windows":
        print "Platform: Windows\r\n"
        srcFolder = srcFolder.replace("/", "\\")
        destFolder = destFolder.replace("/", "\\")
        subprocess.call("xcopy %s %s /E /Y /C" % (srcFolder, destFolder), shell=True)
    elif platform.system() == "Linux":
        print "Platform: Linux\r\n"
        subprocess.call("cp -R %s %s" % (srcFolder + "/*", destFolder), shell=True)
    else:
        print "Platform: Unknown platform: %s\r\n" % (platform.system())
        exit(1)


def DelFolder(srcFolder):
    Logger.INFO("Deleting folder :" + srcFolder)
    if platform.system() == "Windows":
        srcFolder = srcFolder.replace("/", "\\")
        subprocess.call("del %s /Q" % (srcFolder), shell=True)
    elif platform.system() == "Linux":
        Logger.WARNING("Platform: Linux\r\n, we don't rm the folder, use mv instead")
        subprocess.call("/bin/rm -rf %s" % (srcFolder), shell=True)
    else:
        print "Platform: Unknown platform: %s\r\n" % (platform.system())
        exit(1)


def chkPathExist(targetPath):
    if targetPath == "":
        Logger.ERROR("targetPath is empty!!!")
        exit(1)
    #判断该path是否存在，存在返回ture，不存在返回false
    if os.path.exists(targetPath) != True:
        Logger.ERROR("targetPath not exists!!! " + targetPath)
        exit(1)


# warning when array size = 0
def chkArrSize(array):
    if len(array) == 0:
        Logger.WARNING("Array size = 0")
        return False
    return True


# error when array size = 0 and exit the program
def chkArrSizeFail(array):
    if len(array) == 0:
        Logger.ERROR("Array size = 0")
        exit(0)


def cleanUpGens(WORKSPACE, folders):
    Logger.INFO("Clean up: " + WORKSPACE)
    print folders
    if len(folders) != 0:
        for folder in folders:
            try:
                Logger.INFO("Clean up: " + folder)
                if os.path.exists(WORKSPACE + folder):
                    shutil.rmtree(WORKSPACE + folder)
            except Exception as ex:
                Logger.ERROR("cleanUpGens failed")
                print ex


def getFileMD5(pathToFile):
    ret = ""
    if os.path.exists(pathToFile) != True:
        Logger.WARNING("getFileMD5: File not exists: " + pathToFile)
    elif os.path.isfile(pathToFile) != True:
        Logger.WARNING("getFileMD5: PathToFile is not a file: " + pathToFile)
    else:
        md = hashlib.md5()
        fi = open(pathToFile, "rb")
        size = os.path.getsize(pathToFile)
        ti = time.time()
        try:
            while True:
                by = fi.read(8096)
                if not by:
                    break
                else:
                    md.update(by)
            ret = md.hexdigest().upper()
            ti = time.time() - ti
            Logger.INFO(("getFileMD5: total cost: %s sec, file size %f" % (ti, size)))
        except Exception as ex:
            Logger.ERROR("getFileMD5: Read file failed!")
            print ex
        finally:
            fi.close()
    return ret


def searchString(text, pattern):
    """ test: 被搜索的源字符串
        pattern: 正则表达式语法
        index: 要获取的分组结果索引
    """
    m = re.search(pattern, text)
    if m:
        return m.group(0)


def ReplaceFileContent(filename, srcpattern, dsttext):
    '''替换文件中的内容,支持正则表达式语法'''
    file = open(filename, "r")
    lines = file.readlines()
    bFound = False
    output = ""
    for line in lines:
        findstr = searchString(line, srcpattern)
        if findstr:
            print "Find Text:" + findstr
            line = line.replace(findstr, dsttext)
            bFound = True
        output = output + line
    file.close()

    new_file = open(filename, "w")
    new_file.writelines(output)
    new_file.close()
    return bFound


def ReplaceFileContentDebugTool(filename, srcpattern, dsttext):
    '''替换文件中的内容,支持正则表达式语法'''
    file = open(filename, "r")
    lines = file.readlines()
    bFound = False
    output = ""
    for line in lines:
        findstr = searchString(line, srcpattern)
        if findstr:
            print "Find Text:" + findstr
            line = line.replace(line, dsttext)
            bFound = True
        output = output + line
    file.close()

    new_file = open(filename, "w")
    new_file.writelines(output)
    new_file.close()
    return bFound


def findInFile(path_file, pattern):
    """ path_file: 文件路径
        pattern: 正则表达式语法
    """
    ret = False
    file = open(path_file, "r")
    lines = file.readlines()
    for line in lines:
        findstr = searchString(line, pattern)
        if findstr:
            ret = True
            break
    file.close()
    return ret


def CoverFile(path_file, content):
    """
    覆盖文件的内容
    """
    try:
        _file = open(path_file, "w")
        _file.writelines(content)
        _file.close()
    except IOError as err:
        print("File Error:" + str(err))
        return False
    return True


def ChooseFileContentDebugTool(filename, choices):
    file = open(filename, "r")
    if len(choices) != 0:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except:
            print "Error:cannot parse file:"+filename
            sys.exit(1)
        content = root.getchildren()[0]
        print content.tag  + "=====" + str(content.attrib["{http://schemas.android.com/apk/res/android}layout_width"])
        children = content.getchildren()
        debugConfig = {}
        debugConfig["monitor"] = 2
        debugConfig["debug"] = 4
        debugConfig["env"] = 6
        debugConfig["protocol"] = 7
        debugConfig["requst_log"] = 9
        debugConfig["lvProtocolWs"] = 11
        debugConfig["lvNetworkRetryWhite"] = 13
        debugConfig["lvNetworkBackgroundWhite"] = 15
        debugConfig["serverIP"] = 17
        debugConfig["cashierIP"] = 19
        debugConfig["hybridIP"] = 21
        debugConfig["analytics"] = 23
        debugConfig["module"] = 25
        debugConfig["module_param"] = 27
        debugConfig["routemap"] = 29
        debugConfig["rn"] = 31
        debugConfig["llDumpDbFile"] = 33
        debugConfig["scan_download"] = 35
        debugConfig["scan_platform"] = 37
        debugConfig["slipBack"] = 39
        for child in choices:
            print "hhaha" + str(children[debugConfig[child]])
            if debugConfig[child] != 6:
                content.remove(children[debugConfig[child]])
                content.remove(children[debugConfig[child]+1])
            else:
                content.remove(children[debugConfig[child]])
        tree.write(filename, encoding="utf-8",xml_declaration=True)
    else:
        exit(1)


def stringToList(string):
    list1 = string.split(",")
    return list1




