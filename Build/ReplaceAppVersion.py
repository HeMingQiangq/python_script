import re, sys, getopt
import ChangeRNVersionNum

WORKSPACE = ''
VERSION_CODE = ''
RN_JOB_NAME = ''
IS_ALLOW_CHANGE_RN_VERSION = 'true'


def getParam(workspace, version_number, rn_job_name, is_allow_change_rnversion):
    manifest_path = '/jDB/src/main/AndroidManifest.xml'
    gradle_path = '/jDB/build.gradle'
    manifest_all_path = workspace + manifest_path
    gradle_all_path = workspace + gradle_path
    #去掉传如version_number中到"."
    versioncode = str(version_number).replace('.', '')
    versionname = version_number

    # replace manifest version
    replaceVersionNumberOfFile(manifest_all_path, versioncode, 'android:versionCode=.\d{3}.')
    replaceVersionNumberOfFile(manifest_all_path, versionname, 'android:versionName=.\d\.\d\.\d.')
    replaceVersionNumberOfFile(manifest_all_path, versionname, 'android:value=.\d\.\d\.\d.')

    # replace gradle version
    replaceVersionNumberOfFile(gradle_all_path, versioncode, 'versionCode.\d{3}')
    replaceVersionNumberOfFile(gradle_all_path, versionname, 'versionName..\d\.\d\.\d.')

    # change RN version number
    ChangeRNVersionNum.assembleParam(workspace, versioncode, rn_job_name, is_allow_change_rnversion)


def replaceVersionNumberOfFile(file_path, new_version_number, pattern):
    with open(file_path) as File:
        js_content = File.read()
    #比如versionnum == 2.9.3,替换后为293
    if len(new_version_number) == 3:
        reg = pattern
        regcomplie = re.compile(reg)
       # result == 293
        result = regcomplie.findall(js_content)
        if len(result) == 1:
            current_str = result[0]
            reg_str = r'.+(\d{3})'
            reg_strcomplie = re.compile(reg_str)
            current_version = reg_strcomplie.findall(current_str)
            if len(current_version) == 1:
                new_str = current_str.replace(current_version[0], new_version_number)
                new_js_content = js_content.replace(result[0], new_str)
                open(file_path, 'w').write(new_js_content)
    else:
        reg = pattern
        regcomplie = re.compile(reg)
        result = regcomplie.findall(js_content)
        if len(result) == 1:
            current_str = result[0]
            reg_str = r'.+(\d\.\d\.\d)'
            reg_strcomplie = re.compile(reg_str)
            current_version = reg_strcomplie.findall(current_str)
            if len(current_version) == 1:
                new_str = current_str.replace(current_version[0], new_version_number)
                new_js_content = js_content.replace(result[0], new_str)
                open(file_path, 'w').write(new_js_content)


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "w:v:r:c")
    for op, value in opts:
        if op == "-w":
            WORKSPACE = value
        elif op == "-v":
            VERSION_CODE = value
        elif op == "-r":
            RN_JOB_NAME = value
        elif op == "-c":
            IS_ALLOW_CHANGE_RN_VERSION = value

    getParam(WORKSPACE, VERSION_CODE, RN_JOB_NAME, IS_ALLOW_CHANGE_RN_VERSION)
