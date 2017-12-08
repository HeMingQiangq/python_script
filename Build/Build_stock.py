# -*- coding: utf-8 -*-
import shutil, os, sys
import Logger, Util, Const


def copyConfigFile():
    """拷贝ant.properties、product.keystore到主工程目录"""
    dir_project = Const.PROJECT_MAIN[0]['path']
    Util.copyFile(Const.PATH_ANT_PROPERTIES, dir_project)
    Util.copyFile(Const.PATH_LOCAL_PROPERTIES, dir_project)
    Util.copyFile(Const.PATH_KEYSTORE, dir_project)


def copyPropertiesFile():
    """拷贝project.properties到主工程目录"""
    dir_project = Const.PROJECT_MAIN[0]['path']
    if ALLOW_DEBUG_TOOL == "true":
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
                            Const.STR_APPNAME_NEW_STOCK + BUILD_NUMBER)


def ChangeDebuggable():
    """修改AndroidManifest.xml文件中是否有android:debuggable配置"""
    debuggable = 'android:debuggable="false"'
    if BUILD_TYPE == "debug":
        debuggable = 'android:debuggable="true"'
    Util.ReplaceFileContent(WORKSPACE + Const.PATH_MANIFEST, 'android:debuggable\s*=\s*"(true|false)"', debuggable)


def modifyChannelID():
    Util.CoverFile(WORKSPACE + Const.PATH_SOURCEID, CHANNEL_ID)


def ChangeAllowDebugTool():
    """根据参数，开启/关闭摇一摇"""
    dir_project = Const.PROJECT_MAIN[0]['path']
    print "close debugTool(yaoyiyao)"
    if ALLOW_DEBUG_TOOL == "false":
        Util.ReplaceFileContentDebugTool(WORKSPACE + Const.PATH_Build_Gradle, "debugTool", "")


# =================MAIN====================#
def doBuild():
    Logger.INFO("[======begin build...======]")

    Util.chkPathExist(WORKSPACE)
    os.chdir(WORKSPACE)
    Util.chkPathExist(Const.PATH_SCRIPT)
    modifyChannelID()

    ChangeDebuggable()
    ChangeAllowDebugTool()
    if NEED_CHANGENAME == "true":
        modifyAppName()
    # modifyBuildXml()
    # copyConfigFile()
    # copyBuildXml()
    # copyPropertiesFile()


argLen = len(sys.argv)
if (argLen < 8):
    Logger.ERROR('参数个数错误！')
    exit(1)
WORKSPACE = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
ANDROID_HOME = sys.argv[3]
NEED_CHANGENAME = sys.argv[4]
BUILD_TYPE = sys.argv[5]
CHANNEL_ID = sys.argv[6]
ALLOW_DEBUG_TOOL = sys.argv[7]
doBuild()
