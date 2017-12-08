import re
import Util, download_RNBundle


def assembleParam(workspace, version_number, rn_job_name, is_allow_change_rnversion):
    path_suffix = '/jDB/src/main/assets/'
    base_path = workspace + path_suffix
    bundle_path = base_path + 'main.bundle'

    # delete mian.jsbundle & download new main.jsbundle
    if rn_job_name != '':
        save_bundle_path = base_path
        download_RNBundle.execute(rn_job_name, save_bundle_path, version=version_number)
        # if is_allow_change_rnversion == 'true':
        #     rn_version_number = str(version_number).replace('.', '')
        #     replaceRNVersionNumberOfjs(bundle_path, rn_version_number)


def replaceRNVersionNumberOfjs(js_path, new_rn_version):
    with open(js_path) as File:
        js_content = File.read()
    reg = r'.\w=\d{4},\w='
    regcomplie = re.compile(reg)
    result = regcomplie.findall(js_content)
    if len(result) == 1:
        current_str = result[0]
        reg_str = r'\w=(\d{3})\d,\w='
        reg_strcomplie = re.compile(reg_str)
        current_version = reg_strcomplie.findall(current_str)
        if len(current_version) == 1:
            new_str = current_str.replace(current_version[0], new_rn_version)
            print result[0]
            print new_str
            new_js_content = js_content.replace(result[0], new_str)
            open(js_path, 'w').write(new_js_content)
        else:
            print 'keep current version'
