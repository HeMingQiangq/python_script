# -*- coding: utf-8 -*-

import sys, re


# 获取文件内容,以list形式输出
def getFileContent(gradle_path):
    with open(gradle_path) as File:
        gradle_content = File.readlines()
    return gradle_content


# 重写gradle文件内容
def rewriteGradleFileContent(gradle_path, gradle_file_content):
    new_file_content = ''
    for line in gradle_file_content:
        new_file_content += line
    open(gradle_path, 'w').write(new_file_content)


# list中向上插入元素
def insertSingingConfigs(gradle_path, query_string, replace_string):
    gradle_file_content = getFileContent(gradle_path)

    if type(replace_string) == list:
        if query_string in gradle_file_content:
            insert_location = gradle_file_content.index(query_string)
            for line in replace_string:
                gradle_file_content.insert(insert_location, line)
                insert_location += 1
    else:
        if query_string in gradle_file_content:
            insert_location = gradle_file_content.index(query_string)
            gradle_file_content.insert(insert_location, replace_string)
    rewriteGradleFileContent(gradle_path, gradle_file_content)


# list中向下插入元素
def afterInsertSingingConfigs(gradle_path, query_string, replace_string):
    gradle_file_content = getFileContent(gradle_path)

    if type(replace_string) == list:
        if query_string in gradle_file_content:
            insert_location = gradle_file_content.index(query_string) + 1
            for line in replace_string:
                gradle_file_content.insert(insert_location, line)
                insert_location += 1
    else:
        if query_string in gradle_file_content:
            insert_location = gradle_file_content.index(query_string) + 1
            gradle_file_content.insert(insert_location, replace_string)
    rewriteGradleFileContent(gradle_path, gradle_file_content)


# 删除注释行并增加新内容
def delateCommentLine(gradle_path, location, addindex, replace_string):
    gradle_file_content = getFileContent(gradle_path)

    location_index = gradle_file_content.index(location)
    del gradle_file_content[location_index]
    delate_range = range(location_index, location_index + addindex)
    for i in delate_range:
        del gradle_file_content[location_index]
        i += 1

    for line in replace_string:
        gradle_file_content.insert(location_index, line)
        location_index += 1

    rewriteGradleFileContent(gradle_path, gradle_file_content)


# 修改apk名称
def changeAPKName(gradle_path):
    with open(gradle_path) as File:
        gradle_file_content = File.read()
    reg = r',(.+defaultConfig.versionName.+) ".apk"'
    reComplie = re.compile(reg)
    result = reComplie.findall(gradle_file_content)
    for i in result:
        new_file = gradle_file_content.replace(i, '')
    open(gradle_path, 'w').write(new_file)


if __name__ == '__main__':
    # get file content
    SIGNING_CONFIGS = 'addReleaseForGradle/key.txt'
    REPLACE_BEFORE = 'addReleaseForGradle/replace_before.txt'
    REPLACE_AFTER = 'addReleaseForGradle/replace_after.txt'
    # DEBUG_APK = 'addReleaseForGradle/debug_apk.txt'
    SIGNING_CONFIGS_LIST = getFileContent(SIGNING_CONFIGS)
    REPLACE_BEFORE_LIST = getFileContent(REPLACE_BEFORE)
    REPLACE_AFTER_LIST = getFileContent(REPLACE_AFTER)
    # DEBUG_APK_LIST = getFileContent(DEBUG_APK)

    # gradle path
    WORKSPACE = sys.argv[1]
    GRADLEFILE_PATH = WORKSPACE + '/jDB/build.gradle'

    # BUILDTYPES = REPLACE_BEFORE_LIST[0]
    APPLICATION_VARIANTS = REPLACE_BEFORE_LIST[1]
    SIGNING_CONFIGS_LINE = REPLACE_BEFORE_LIST[6]
    # COMMENT_DEBUG_APK = REPLACE_BEFORE_LIST[2]
    DEV = REPLACE_BEFORE_LIST[5]

    SIGNCONFIGS_RELEASE = REPLACE_AFTER_LIST[0]
    # ZIPALIGNENABLED = REPLACE_AFTER_LIST[1]

    afterInsertSingingConfigs(GRADLEFILE_PATH, SIGNING_CONFIGS_LINE, SIGNING_CONFIGS_LIST)
    insertSingingConfigs(GRADLEFILE_PATH, APPLICATION_VARIANTS, SIGNCONFIGS_RELEASE)
    # insertSingingConfigs(GRADLEFILE_PATH, SIGNCONFIGS_RELEASE, ZIPALIGNENABLED)
    afterInsertSingingConfigs(GRADLEFILE_PATH, DEV, SIGNCONFIGS_RELEASE)

    # delateCommentLine(GRADLEFILE_PATH, COMMENT_DEBUG_APK, 10, DEBUG_APK_LIST)
    # afterInsertSingingConfigs(GRADLEFILE_PATH, replace_before_list[2], debug_apk_list)

    changeAPKName(GRADLEFILE_PATH)
