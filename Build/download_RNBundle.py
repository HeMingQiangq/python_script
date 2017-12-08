# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
# from bs4 import BeautifulSoup,Tag,CData
import urllib, re, os, sys, requests


def gethtml(url):
    page = urllib.urlopen(url)
    Html = page.read()
    return Html


# def get_bundle_resource(html_content, job_url, save_bundle_path):
#     soup = BeautifulSoup(html_content, fromEncoding='utf8')
#     # base_apk_url = soup.find('a', href=re.compile(r'.+Android_Bundle/main.zip'))
#     base_apk_url = 'artifact/Android_Bundle/main.zip'
#     if base_apk_url != '':
#         os.system('rm -f ' + save_bundle_path + 'main.zip')
#         all_apk_url = job_url + base_apk_url['href']
#         save_path = os.path.join(save_bundle_path, 'main.zip')
#         urllib.urlretrieve(all_apk_url, save_path)
#         # os.system('rm -f ' + save_bundle_path + 'drawable-xhdpi.zip')
#         # os.system('rm -f ' + save_bundle_path + 'main.bundle')
#         # os.system('rm -f ' + save_bundle_path + 'rnVersion.txt')
#         # os.system('unzip ' + save_bundle_path + 'main.zip' + ' -d ' + save_bundle_path)

def get_bundle_resource(html_content, job_url, save_bundle_path):
    try:
        requestsMainMd5 = 'requestsMainMd5'
        localMainMd5 = 'localMainMd5'
        requestsPackerMd5 = 'requestsPackerMd5'
        localPackerMd5 = 'localPackerMd5'
        mainMd5IsEqual = 1
        packerMd5IsEqual = 1
        # soup = BeautifulSoup(html_content, fromEncoding='utf8')
        # base_apk_url = soup.find('a', href=re.compile(r'.+iOS_Bundle/main.zip'))
        base_apk_url = 'lastSuccessfulBuild/artifact/Android_Bundle/main.zip'
        if base_apk_url != '':
            # all_apk_url = job_url + base_apk_url['href']
            all_apk_url = job_url + base_apk_url
            save_path = os.path.join(save_bundle_path, 'main.zip')
            os.system('rm -f ' + save_bundle_path + 'main.zip')
            urllib.urlretrieve(all_apk_url, save_path)
            base_main_md5 = 'lastSuccessfulBuild/artifact/Android_Bundle/md5_Android_main.txt'
            all_main_md5 = job_url + base_main_md5
            requestsMainMd5 = requests.get(all_main_md5).text
            requestsMainMd5 = requestsMainMd5.replace('\n', '')
            print 'request main.zip md5 is:', requestsMainMd5
            localMainMd5 = os.popen('md5 -q {0}'.format(save_path)).read()
            localMainMd5 = localMainMd5.replace('\n', '')
            print 'local main.zip md5 is:', localMainMd5
            mainMd5IsEqual = cmp(localMainMd5, requestsMainMd5)

            # os.system('rm -f ' + save_bundle_path + 'assets.zip')
            # os.system('rm -f ' + save_bundle_path + 'main.jsbundle')
            # os.system('rm -f ' + save_bundle_path + 'rnVersion.txt')
            # Util.ExecCmd('unzip ' + save_bundle_path + 'main.zip' + ' -d ' + save_bundle_path)

        # soup = BeautifulSoup(html_content, fromEncoding='utf8')
        # base_apk_url = soup.find('a', href=re.compile(r'.+iOS_Bundle/packer.zip'))
        base_apk_url = 'lastSuccessfulBuild/artifact/Android_Bundle/packer.zip'
        if base_apk_url != '':
            all_apk_url = job_url + base_apk_url
            save_path = os.path.join(save_bundle_path, 'packer.zip')
            os.system('rm -f ' + save_bundle_path + 'packer.zip')
            urllib.urlretrieve(all_apk_url, save_path)
            base_packer_md5 = 'lastSuccessfulBuild/artifact/Android_Bundle/md5_Android_packer.txt'
            all_packer_md5 = job_url + base_packer_md5
            requestsPackerMd5 = requests.get(all_packer_md5).text
            requestsPackerMd5 = requestsPackerMd5.replace('\n', '')
            print 'request packer.zip md5 is:', requestsPackerMd5
            localPackerMd5 = os.popen('md5 -q {0}'.format(save_path)).read()
            localPackerMd5 = localPackerMd5.replace('\n', '')
            print 'local packer.zip md5 is:', localPackerMd5
            packerMd5IsEqual = cmp(localPackerMd5, localPackerMd5)

        checkdic = {'mainMd5IsEqual': mainMd5IsEqual, 'packerMd5IsEqual': packerMd5IsEqual}
        return checkdic

    except Exception as e:
        print 'ERROR: RN Embedded Failure.', e
# 添加校验md5次数
def checkRNRequestsFrequency(html_content, job_url, save_bundle_path):
    frequency = 3
    while frequency > 0:
        isEqual = get_bundle_resource(html_content, job_url, save_bundle_path)
        if isEqual['mainMd5IsEqual'] == 0:
            if isEqual['packerMd5IsEqual'] == 0:
                frequency = 0
            else:
                frequency -= 1
                print 'packerMd5 is not Equal'
        else:
            frequency -= 1
            print 'mainMd5 is not Equal'

def get_bundle_url(data):
    http_url = 'http://43.227.141.152/version/getYumaiPack'
    r = requests.post(http_url, data=data)
    t = r.json()
    return_code = t['error']['returnCode']
    if return_code == 0:
        data = t["data"]
        download_link = data["downloadLink"]
        return download_link
    else:
        return False


def get_bundle_hybrid(version, save_bundle_path):
    data = {
        'platform': 'android',
        'version': version
    }
    url = get_bundle_url(data)
    print 'Hybrid预埋包下载地址: ', url
    os.system('echo {url}'.format(url=url))
    if url is None:
        for i in range(1, 6):
            url = get_bundle_url(data)
            if url:
                break
    if url is not None:
        save_path = os.path.join(save_bundle_path, 'hybrid.zip')
        os.system('rm -f ' + save_bundle_path + 'hybrid.zip')
        urllib.urlretrieve(url, save_path)


def execute(rn_job_name, save_bundle_path, version):
    jenkins_url = 'http://client-jenkins.jdb-dev.com:8080'
    tag = 'job'
    split = '/'

    job_url = jenkins_url + split + tag + split + rn_job_name + split
    html_content = gethtml(job_url)
    checkRNRequestsFrequency(html_content, job_url, save_bundle_path)
    # get_bundle_hybrid(version=version, save_bundle_path=save_bundle_path)
