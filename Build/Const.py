# -*- coding: utf-8 -*-
import os

# 脚本相关配置
PATH_SCRIPT = 'script/Build'
PATH_CODE = ""
PATH_BUILD_XML = PATH_SCRIPT + '/module/build_base.xml'
PATH_BUILD_XML = PATH_SCRIPT + '/module/build.xml'
PATH_ANT_PROPERTIES = PATH_SCRIPT + '/module/ant.properties'
PATH_LOCAL_PROPERTIES = PATH_SCRIPT + '/module/local.properties'
PATH_PROPERTIES = PATH_SCRIPT + '/properties/'
PATH_KEYSTORE = PATH_SCRIPT + '/module/renrenxing.keystore'

# build.xml中SDK_PATH
STR_SDK_PATH = 'SDK_PATH'
STR_SRC_DIR = 'SRC_DIR'

STR_APPNAME_OLD = '@string/app_name'
STR_APPNAME_NEW = '借贷宝'
STR_APPNAME_NEW_STOCK = '九州内测版'
STR_DEBUGGABLE_DEFAULT = 'android:debuggable="true"'

STR_CONFIG_DEBUGTOOL = 'ALLOW_DEBUG_TOOL\s*=\s*(false|true)'
STR_CONFIG_DEBUGTOO_FALSE = r'ALLOW_DEBUG_TOOL = false'
STR_CONFIG_DEBUGTOO_TRUE = r'ALLOW_DEBUG_TOOL = true'

# 项目配置部分
JDB = {'name': 'jDB', 'path': PATH_CODE + '/jDB', 'srcdir': 'src:adp:toolkit'}
LIB_IMAGELOADER = {'name': 'lib_imageloader', 'path': PATH_CODE + '/lib_imageloader', 'srcdir': 'src'}
LIB_HELLOCHARTS = {'name': 'lib_hellocharts', 'path': PATH_CODE + '/lib_hellocharts', 'srcdir': 'src'}
# the XCL_CHARTS is deleted
# XCL_CHARTS = {'name':'XCL-Charts',  'path':PATH_CODE + '/XCL-Charts', 'srcdir':'src'}
DEBUGTOOL = {'name': 'debugTool', 'path': PATH_CODE + '/debugTool', 'srcdir': 'src'}

PROJECT_MAIN = [JDB]
PROJECT_OTHER = [LIB_IMAGELOADER, LIB_HELLOCHARTS, DEBUGTOOL]
PROJECT_ALL = PROJECT_MAIN + PROJECT_OTHER

PATH_MANIFEST = PROJECT_MAIN[0]['path'] + '/src/main/AndroidManifest.xml'
PATH_SOURCEID = PROJECT_MAIN[0]['path'] + '/src/main/assets/sourceid.dat'
PATH_EMBEDDED_HYBRID = PROJECT_MAIN[0]['path'] + '/src/main/assets/'
PATH_JDB_CONFIG = PROJECT_MAIN[0]['path'] + '/src/com/rrh/jdb/JDBConfig.java'
PATH_Build_Gradle = PROJECT_MAIN[0]['path'] + '/build.gradle'

PATH_DebugTool_View = PROJECT_OTHER[2]['path'] + '/src/main/res/layout/adp_debug_config_activity.xml'

# print PROJECT_ALL

#Jenkins地址配置
JENKINS_HOST = "http://client-jenkins.jdb-dev.com:8080"

#一键发布平台配置
CHANNEL_HOST = "http://100.73.14.15:8080/channelPublish"