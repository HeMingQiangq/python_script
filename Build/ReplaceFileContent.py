import os, sys


def ReplaceFileContent(filename, srctext, dsttext):
    file = open(filename, "r")
    lines = file.readlines()
    ret = ""
    for line in lines:
        if line.find(srctext) != -1:
            print "Find Text:" + srctext
            line = line.replace(srctext, dsttext)
        ret = ret + line;
    file.close();

    new_file = open(filename, "w")
    new_file.writelines(ret)
    new_file.close()


if __name__ == '__main__':
    argLen = len(sys.argv)
    if (argLen < 4):
        exit(0)
    FILE_NAME = sys.argv[1]
    SRC_TEXT = sys.argv[2]
    DST_TEXT = sys.argv[3]
    ReplaceFileContent(FILE_NAME, SRC_TEXT, DST_TEXT)
