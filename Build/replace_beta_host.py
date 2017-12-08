import os, sys


def ReplaceFileContent(filename, product_host, beta_host):
    file = open(filename, "r")
    lines = file.readlines()
    ret = ""
    for line in lines:
        if line.find(product_host) != -1:
            print "Find Text:" + product_host
            line = line.replace(product_host, beta_host)
        ret = ret + line
    file.close()

    new_file = open(filename, "w")
    new_file.writelines(ret)
    new_file.close()


if __name__ == '__main__':
    argLen = len(sys.argv)
    if (argLen < 1):
        exit(0)
    FILE_NAME = sys.argv[1]
    PRODUCT_HOST = "https://tradeapi.jiedaibao.com/\";"
    BETA_HOST = "http://beta-tradeapi.jiedaibao.com/\";"
    ReplaceFileContent(FILE_NAME, PRODUCT_HOST, BETA_HOST)
