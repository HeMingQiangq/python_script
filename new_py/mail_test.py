# --**coding: utf-8**


import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, os
from email.mime.text import MIMEText

build = "/Users/hemingqiang/Documents/code/android/Jenkins_Android/hemq_Jenkins_Android/Build"
file = "html_content.txt"
filepath = os.path.join(build, file)
messagee = '''
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <p align="center"><font color="red" size="5">Android_CI_Branch_Findbugs静态代码检查报告:</font></p>
    构建状态：$BUILD_STATUS<br/>
    项目地址：<a href="$PROJECT_URL" style="color:blue">点击查看</a><br/>
    报告地址：<a href="${BUILD_URL}findbugsResult"  style='color:blue'>点击查看</a><br/><hr/>
    ${FILE,path="${WORKSPACE}/summaryxml.html"}<br/><hr/>

    '''


def __init__(self):
    # 获取所有需要的邮件地址
    # address_to = self.get_email_address('to')
    # address_cc = self.get_email_address('cc')
    self.version = os.getenv('VERSION')
    self.address_to = 'hemq@jiedaibao.com'
    self.address_cc = ''
    self.address_from = '17300142501@163.com'
    self.address_from_pwd = "He1995102030"
    self.email_subject = 'Android端静态代码检查报告！！！'



def get_email_address(self, address_type):
    return open('email_%s' % address_type, 'r').readline()


def read_html(file):

    file =open(file,"rb")
    file_content = file.read()
    file.close()
    return file_content



def send_email():
    version = os.getenv('VERSION')
    address_to = 'hemq@jiedaibao.com'
    address_cc = ''
    address_from = '17300142501@163.com'
    address_from_pwd = "He1995102030"
    email_subject = 'Android端静态代码检查报告！！！'
    # build_status = findbugs.Build_Ststus
    # build_url = findbugs.Build_Url

    #message = "构建状态：" + build_status + "\r" + "构建地址:" + build_url
    # code_status = findbugs.findbugreport

    #msgg = MIMEText(code_status + "\r" + "\r" + message, 'plain', 'utf-8')
    html_content = read_html(file_name)
    report_content = read_html(file_namem)
    msg = MIMEText(html_content+report_content, _subtype='html', _charset='utf-8')
    msg['From'] = address_from
    msg['To'] = address_to
    # msg['Cc'] = self.address_cc
    msg['Subject'] = gettime() + "\t" + '%s' % email_subject
    # msg.attach(self.get_email_html())

    try:
        s = smtplib.SMTP_SSL('smtp.163.com', 465)
        s.login(address_from, address_from_pwd)
        s.sendmail(address_from, address_to, msg.as_string())
        print "邮件发送完毕，请注意查收"
    except Exception as e:
        print('———— ERROR: %s') % e
        print "email xxxx"


def gettime():
    local_time = time.strftime("%Y/%m/%d", time.localtime())
    # 格式化成2016-03-20 11:45:39形式
    # local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 格式化成Sat Mar 28 22:24:24 2016形式
    # time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    # time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

    return local_time

if __name__ == '__main__':
    #file_path ="/Users/hemingqiang/Documents/code/android/Jenkins_Android/hemq_Jenkins_Android/html"
    file_name = "html.html"
    file_namem = "findbugggg.html"
    #all_file_path = os.path.join(filepath,file_name)
    send_email()

    pass

