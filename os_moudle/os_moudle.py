#--**coding:utf-8**--

import os

#获取当前工作目录

path = os.getcwd()

#获取目录下所有文件名

all_text = os.listdir(path)

#检验某路径指向的是否是个文件,可以用于检验某路径是下否存在该文件
file_name = "2.txt"
split_sign = "/"
last_path = path + split_sign + file_name
another_name = "4.txt"

def write_file(filepath,filename,gradle_content):
    '''
    :param filepath: 文件路径
    判断路径下是否存在该文件，若存在，则写入信息
    若不存在，则新建文件,再写入信息
    '''
    if os.path.isfile(filepath):
        file = open(filename,"w")
        file.write(gradle_content)
        file.close()

    else:
        file = open(filename, "w")
        file.write(gradle_content)
        if len(file.write(gradle_content)) > 0:
            print ""
            file.close()
        else:
            print ""
            file.close()

        file.close()

def remove_file(filepath,filename):
    '''
    :param filepath:路径
    :param filename:文件名
    判断路径下是否存在该文件，若存在，则删除文件
    '''
    if os.path.isfile(filepath):
        os.remove(filepath)
        print "成功删除文件"
    else:
        print "该路径为空"

def is_dir(filepath):
    '''
    判断该路径是否是一个目录
    '''
    dir_path = os.path.isdir(filepath)
    if dir_path:
        print "该路径是目录"
    else:
        print "该目录是不是目录"
        os.listdir(filepath)
def return_dir_and_filename(path):
    '''
    调用该方法，返回一个路径下对文件夹及所有文件名
    '''
    dir_name = os.path.split(path)
    return dir_name

def excute_shell(path):
    dir_name = os.path.split(path)
    dir_name = dir_name[1]
    dd = os.system()
    print dir_name


def printdd():
    JDB = {'name': 'jDB', 'path': 'PATH_CODE'+'/jDB', 'srcdir': 'src:adp:toolkit'}
    PROJECT_MAIN = [JDB]
    PATH_MANIFEST = PROJECT_MAIN[0]['path'] + '/src/main/AndroidManifest.xml'

if __name__ == '__main__':
    #write_file(last_path,"2.txt","gradle2.14.1-all")
    #remove_file(last_path,file_name)
    #is_dir(last_path)
    dir_name =return_dir_and_filename(path)
    excute_shell(path)

