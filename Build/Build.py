# -*- coding: utf-8 -*-
import shutil, os, sys, getopt, requests, urllib
import Logger, Util, Const
import ReplaceAppVersion

def copyConfigFile():
    """拷贝ant.properties、product.keystore到主工程目录"""
    dir_project = Const.PROJECT_MAIN[0]['path']
    Util.copyFile(Const.PATH_ANT_PROPERTIES, dir_project)
    Util.copyFile(Const.PATH_LOCAL_PROPERTIES, dir_project)
    Util.copyFile(Const.PATH_KEYSTORE, dir_project)


def copyPropertiesFile():
    """拷贝project.properties到主工程目录."""
    dir_project = Const.PROJECT_MAIN[0]['path']
    if IS_SHAKE == "true":
        name_properties = Const.PROJECT_MAIN[0]['name'] + '_debug.project.properties'
    else:
        name_properties = Const.PROJECT_MAIN[0]['name'] + '.project.properties'
    Util.copyFile(WORKSPACE + Const.PATH_PROPERTIES + name_properties, dir_project + '/project.properties')


def copyBuildXml():
    """拷贝build.xml到所有目录"""
    for project in Const.PROJECT_ALL:
        Util.copyFile(Const.PATH_BUILD_XML, project['path'])
        Util.ReplaceFileContent(project['path'] + r'/build.xml', Const.STR_SRC_DIR, project['srcdir'])


def modifyBuildXml():
    Util.ReplaceFileContent(Const.PATH_BUILD_XML, Const.STR_SDK_PATH, ANDROID_HOME)
    Util.ReplaceFileContent(Const.PATH_LOCAL_PROPERTIES, Const.STR_SDK_PATH, ANDROID_HOME)


def modifyAppName():
    """在APPNAME后面加上BUILD_NUMBER，发版时注意去掉"""
    Util.ReplaceFileContent(WORKSPACE + Const.PATH_MANIFEST, Const.STR_APPNAME_OLD,
                            Const.STR_APPNAME_NEW + BUILD_NUMBER)


def ChangeDebuggable():
    """修改AndroidManifest.xml文件中是否有android:debuggable配置"""
    debuggable = 'android:debuggable="false"'
    if BUILD_TYPE != "release":
        debuggable = 'android:debuggable="true"'
    Util.ReplaceFileContent(WORKSPACE + Const.PATH_MANIFEST, 'android:debuggable\s*=\s*"(true|false)"', debuggable)

#Const.PATH_SOURCEID = PROJECT_MAIN[0]['path'] + '/src/main/assets/sourceid.dat'
def modifyChannelID():
    Util.CoverFile(WORKSPACE + Const.PATH_SOURCEID, CHANNEL_ID)


#def ChangeAllowDebugTool():
    """根据参数，开启/关闭摇一摇"""
    dir_project = Const.PROJECT_MAIN[0]['path']
#    print "close debugTool(yaoyiyao)"
#    if IS_SHAKE == "false":
#        Util.ReplaceFileContentDebugTool(WORKSPACE + Const.PATH_Build_Gradle, "debugTool", "")

def ChangeAllowDebugTool():
    """根据参数，开启/关闭摇一摇"""
    dir_project = Const.PROJECT_MAIN[0]['path']
    print "close debugTool(yaoyiyao)"
    if IS_SHAKE == "false":
        Util.ReplaceFileContentDebugTool(WORKSPACE + Const.PATH_Build_Gradle, "debugTool", "")

def embedded_hybrid():
    requestsmd5 = 'requestsMd5'
    localMd5 = 'localMd5'
    path = os.path.join(WORKSPACE + Const.PATH_EMBEDDED_HYBRID, 'hybrid.zip')
    payload = {
        "platform": "android",
        "version": VERSION,
        "appID": 0
    }
    with requests.session() as s:
        try:
            r = s.post('http://43.227.141.152/version/getYumaiPack', payload)
            response = r.json()
            download_link = response["data"]["downloadLink"]
            requestsmd5 = response['data']['md5']
            urllib.urlretrieve(download_link, path)
            localMd5 = os.popen('md5 -q {0}'.format(path)).read()
            print '===== INFO =====: Embedded Hybrid Successful from: ', download_link
            print '===== INFO =====: Embedded Hybrid MD5: ', requestsmd5
            print '===== INFO =====: Embedded Hybrid Successful to: ', path
        except Exception as e:
            print 'ERROR: Hybrid Embedded Failure.', e
    localMd5 = localMd5.replace('\n', '')
    return cmp(requestsmd5, localMd5)

def checkRequestsFrequency():
    frequency = 3
    while frequency > 0:
        isEqual = embedded_hybrid()
        if isEqual != 0:
            frequency -= 1
        else:
            frequency = 0

def embedded_getCodeFile():
    path = os.path.join(WORKSPACE + Const.PATH_EMBEDDED_HYBRID, 'getCodeFile.txt')
    payload = {
        'clientVersion': VERSION,
        'memberID' : '505339670746991581',
        'platform' : 'android'
    }
    with requests.session() as s:
        try:
            r = s.post('http://tradeapi.jiedaibao.com/mybankv21/phpsync/sync/hybrid/getCodeFile', payload)
            response = r.json()
            if len(response['data']['rnPackerFileList']):
                getcodefile = r.content
                f = open(path, 'w')
                f.truncate()
                f.write(getcodefile)
                f.close()
                print '===== INFO: ===== getCodeFile embedded Success. '
            print '===== INFO: ===== getCodeFile does not embedded because rnPackFileList empty. ', \
                response['data']['rnPackerFileList']
        except Exception as e:
            print 'ERROR: getCodeFile.txt Embedded Failure.', e

# =================MAIN====================#
def doBuild():
    Logger.INFO("[======begin build...======]")
    #主要是判断workspace是否存在，不存在返回错误信息
    Util.chkPathExist(WORKSPACE)
    #改变当前工作目录到指定目录
    os.chdir(WORKSPACE)
    #PATH_SCRIPT = 'script/Build'
    Util.chkPathExist(Const.PATH_SCRIPT)
    #覆盖JDBApp／jDB／src／main／AndroidManifest.xml 文件内容，传入参数是channelid
    modifyChannelID()
    # 修改JDBApp／jDB／src／main／AndroidManifest.xml中的 android:debuggable="true"值
    ChangeDebuggable()
    #若打打是release包，会将gradle文件中的denbugtool替换为""，从而实现没有摇一摇
    ChangeAllowDebugTool()
    checkRequestsFrequency()
    embedded_getCodeFile()
    if IS_NEED_CHANGE_NAME == "true":
        modifyAppName()
        # modifyBuildXml()
        # copyConfigFile()
        # copyBuildXml()
        # copyPropertiesFile()


argLen = len(sys.argv)
if (argLen < 7):
    Logger.ERROR('参数个数错误！')
    exit(1)
WORKSPACE = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
ANDROID_HOME = sys.argv[3]
BUILD_TYPE = sys.argv[4]
CHANNEL_ID = sys.argv[5]
VERSION = sys.argv[6]

if BUILD_TYPE == 'release':
    IS_SHAKE = 'false'
    IS_NEED_CHANGE_NAME = 'false'
else:
    IS_SHAKE = 'true'
    IS_NEED_CHANGE_NAME = 'true'

doBuild()
