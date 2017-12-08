#coding=utf-8
import os
import sys
import hashlib
import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from requestH5 import getKeyPath
PADDING = '\0'
#PADDING = ' '
pad_it = lambda s: s+(16 - len(s)%16)*PADDING
key = 'router.jiedaibao'#秘钥
iv = 'router.jiedaibao'#秘钥

# f = raw_input("请输入文件路径")
# type = raw_input("请输入操作 1：加密 2：解密")
f = getKeyPath('android', sys.argv[2])
type = '1'

fileName = str(f)
fileName = fileName.rstrip("\n")
fileName = fileName.rstrip(" ")
fileObject = open(fileName,'r')
encryptStr = fileObject.read()
fileObject.close()
encryptStr = encryptStr.rstrip("\n")
encryptStr = encryptStr.rstrip(" ")


if type == "1":
    generator = AES.new(key, AES.MODE_CBC, iv)
    crypt = generator.encrypt(pad_it(encryptStr))
    cryptedStr = base64.b64encode(crypt)
else:
    generator = AES.new(key, AES.MODE_CBC, iv)
    cryptedStr = generator.decrypt(base64.b64decode(encryptStr))

#########################
fileObject = open(fileName,'w')
fileObject.write(cryptedStr)
fileObject.close()
