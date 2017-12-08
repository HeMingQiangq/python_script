#--**coding:utf-8*8--
import sys,os,re
'''
1.当传参为release包时，去掉摇一摇
2.改变build number

'''

#buildNumber = sys.argv[1]
# buildType = sys.argv[2]
# channelId = sys.argv[3]
release = "release"

def isRelease(buildType):

    if buildType == "release":
        #打开gradle文件，去除摇一摇
        #moudle_path = "os_moudle"
        filepath = "file.html"
        # lastfilepath = moudle_path+"/"+filepath
        #组合路径
        file_path = os.path.join(filepath)
        #print file_path
        with open(file_path) as file:
            file_content = file.read()
            #print  file_content
            file.close
            return file_content

    else:
        print "debug"

def change_gradle(filecontent):
    '''
    利用正则匹配gradle文件找到debugtool
    '''
    pattern = r':debugTool'
    bool = re.search(pattern,filecontent)
    print bool.group()
    print type(bool.group())
    if bool:
        filecontent = str(filecontent)
        filecontent = filecontent.replace(bool.group(),"")
        return filecontent

    else:
        print "未找到要匹配的内容"

def rwriteGradlefile(filecontent):
    i = 1
    if i > 0:
        file = open("build.txt","w")
        file.write(filecontent)
        file.close()
        print "重写gradle成功"
    else:
        print "重写失败"

if __name__ == '__main__':
    filecontent = isRelease(release)
    print filecontent
    # filecontent = change_gradle(filecontent)
    # rwriteGradlefile(filecontent)