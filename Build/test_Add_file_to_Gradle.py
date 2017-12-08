#--**coding:utf-8**--
import re


def writein(gradle_path,str):
    file = open(gradle_path,"w")

    file.writelines(str)

    file.close()


def get_content(txt_path):
    with open(txt_path) as file:
        file_content = file.readlines()
    return file_content

def get_contentt(path):
    with open(path) as file:
        file_content = file.read()
    return file_content

def insert_content(signing_type,index_replace,file_content = get_content("addReleaseForGradle/replace_before.txt")):
    if type(signing_configs) == list:
        if index_replace in file_content:
            insert_location = file_content.index(index_replace) + 1
            for line in file_content:
                file_content.insert(insert_location,line)
                insert_location+=1



#创建方法匹配gradlefile内容
def re_gradlefile(gradle_path):
    # gradlefile_path = "addReleaseForGradle/gradlefile.txt"
    with open(gradle_path) as file:
        file_content = file.read()
    pattern = r',(.+defaultConfig.versionName.+) ".apk"'
    re_content = re.findall(pattern,file_content)
    for temp in re_content:
        new_file = file_content.replace(temp,"")
    open(gradlefile_path,"w").write(new_file)




if __name__ == '__main__':

    reaplace_after_content = "addReleaseForGradle/replace_before.txt"
    reaplace_after_content = get_content(reaplace_after_content)
    index_replace = reaplace_after_content.index(reaplace_after_content[6])
    content  = reaplace_after_content[6]
    SIGNING_CONFIGS = 'addReleaseForGradle/key.txt'
    #获取sining_configs文件内容
    signing_configs = get_content(SIGNING_CONFIGS)
    #print type(signing_configs)
    gradlefile_path = "addReleaseForGradle/gradlefile.txt"
    #gradlefile_content = get_contentt(gradlefile_path)
   # print gradlefile_content
   # re_gradlefile(gradlefile_path)

    str = "293"
    str1 = str[0]
    pattern = r".+(\d{3})"

    # if len(str) == 1 :
    #     con = re.findall(pattern,str1)
    #     print con
    stringg = "wenben"
    cc = writein(gradlefile_path,stringg)
    print cc


