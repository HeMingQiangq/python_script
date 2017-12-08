#usr/bin/python
#coding=utf-8

import os
import urllib2
import urllib



def getKeyPath(platform, clientVersion):
    try:
        url = "http://tradeapi.jiedaibao.com/mybankv21/phpsync/sync/hybrid/getRouterList"
        par = {'platform': platform, 'clientVersion': clientVersion, 'routerListVersion': '0'}
        data = urllib.urlencode(par)
        request = urllib2.Request(url, data)
        response1 = urllib2.urlopen(request)

        text = response1.read()
        print text

        filepath = os.path.abspath('requestH5.py')

        pathArray = filepath.split('/')
        pathArray.remove('requestH5.py')
        pathStr = '/'.join(pathArray)

        keyPath = pathStr + '/jDB/src/main/assets/routerMap.txt'

        f1 = open(keyPath, 'w')
        f1.write(text)
        f1.close()

        return keyPath
    except Exception as e:
        print 'ERROR: routerMap Embedded Failure.', e



