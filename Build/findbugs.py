#--**coding:utf-8**--
import sys,os,re,time
import findbugs_mail
'''
改善报告过于笼统
准备脚本获取每次报告生成的bug个数
判断当日是否需要解决bug
发送邮件至对应人员
邮件信息由此传入
/Users/hemingqiang/Documents/code/android/Jenkins_Android/hemq_Jenkins_Android/Build

'''


# Build_Ststus =sys.argv[0]
# Projec_tUrl = sys.argv[1]
# Build_Url = sys.argv[2]
# Workspace = sys.argv[3]

Build_Ststus ="http:www.baidu.com"
Projec_tUrl = "http:www.baidu.com"
Build_Url = "http:www.baidu.com"
Workspace = "http:www.baidu.com"


def getReport(report_path):
    '''
    :param report_path: report路径，准备外部传入
    return：报告内容
    '''

    all_path = "/Users/hemingqiang/Documents/code/android/Jenkins_Android/hemq_Jenkins_Android/Build"
    report_path = os.path.join(all_path,report_path)
    with open(report_path) as file:
        report_content = file.read()
        return report_content


def dealwith_report(report_content):
    '''
    :param report_content: 处理文件内容
    :return: 获取到到bug数量
    '''
    #创建空列表
    all_bug = []
    bugcount = 0
    pattern = r"Most Buggy Class in Package with(.*?)Bug"
    bug_content = re.findall(pattern,report_content)
    if bug_content:
        #pattern是个gud
        #遍历获取到到各个包的bug数量，改变类型，存入新列表中
        for bug_count in bug_content:
            bug_int =  int(bug_count)
            all_bug.append(bug_int)
        #得出总bug数
        for bugCount in all_bug:
            bugcount+=bugCount
        return bugcount
    else:
        bug_num = 0
        print "================ no bug ============="
        return bug_num
    pass

def mail(bug_number):
    '''
    :param bug_number: 获取到到bugnumber
    :return: 根据此值判断findbug当天结果，并发送邮件
    '''
    if bug_number == 0:
        print"今日代码状一切正常正常"
        findbugreport = "findbug报告，今日代码状态一切正常"
        findbugs_mail.send_email(findbugreport,Build_Ststus,Build_Url)

    elif bug_number > 0 and bug_number <= 5:
        print "今日bug数量%d"% bug_number
        #findbugs_mail.send_email()
    else:
        print ""
        findbugreport = "bug有点多啊！！！"
        findbugs_mail.send_email(findbugreport,Build_Ststus,Build_Url)
    pass

if __name__ == '__main__':
    #report_path =sys.argv[0]
    report_path = "summary.html"
    report_content = getReport(report_path)
    bug_num = dealwith_report(report_content)
    mail(bug_num)

    # 格式化成2016-03-20 11:45:39形式
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    local_time = time.strftime("%Y-%m-%d",time.localtime())

    # 格式化成Sat Mar 28 22:24:24 2016形式
    # time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    # time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

    #print local_time
