import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import sys
import math
import json

#python 3.4.2
#需要在常用电脑上登录,不然会有验证码的问题
#关注获取不全..BUG

#不是男的则统计为姑娘
#匿名用户单独列出

#邮箱和密码
email = 'xx@gmail.com'
password = 'xx'
#答案链接地址
questionurl = 'http://www.zhihu.com/question/26431968'

def ungzip(data):
    try:        # 尝试解压
        #print('正在解压.....')
        data = gzip.decompress(data)
        #print('解压完毕!')
    except:
        #print('未经压缩, 无需解压')
        print(' ')
    return data

def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def getVoteCount(data):
    cer = re.compile('<div class="zm-item-vote-info " data-votecount="(.*)">', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getAnswerId(data):
    cer = re.compile('data-aid="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getPeopleUrl(data):
    cer = re.compile('href="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist

def getGender(data):
    cer = re.compile('<i class="icon icon-profile-male">', flags = 0)
    strlist = cer.findall(data)
    return len(strlist)

def getFollowersCount(data):
    cer = re.compile('followers"><strong>(.*)</strong></a>', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getFollowersPeopleUrl(data):
    cer = re.compile('class="zm-item-link-avatar"\nhref="(.*)"', flags = 0)
    strlist = cer.findall(data)

    #去重复
    jsonStr = {}
    for strElement in strlist:
        jsonStr[strElement] = 0

    strlist = jsonStr.keys()
    return strlist

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

#获取_xsrf
url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)     # 解压
_xsrf = getXSRF(data.decode())
print('获取xsrf完成')

#登录
url += 'login'
postDict = {
        '_xsrf':_xsrf,
        'email': email,
        'password': password,
        'rememberme': 'y'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)
data = data.decode()
loginFlag = data.find('<i class="zg-icon zg-icon-dd-pm"></i>私信')
if(loginFlag == -1):
    print('登录失败')
    sys.exit()
print('登录成功')

#答案链接地址
url = questionurl
op = opener.open(url)
data = op.read()
data = ungzip(data)
followersCountStr = getFollowersCount(data.decode())
followersCountInt = int(int(followersCountStr)/20 ) * 20

#答案关注者地址
url = questionurl + '/followers'
op = opener.open(url)
data = op.read()
data = ungzip(data)
followersInfo = data.decode()
_xsrf = getXSRF(followersInfo)
print('获取xsrf完成')

offset = 20
while True:
    offset += 20

    postDict = {
            'start': 0,
            'offset': offset,
            '_xsrf': _xsrf
    }
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(url, postData)
    data = op.read()
    data = ungzip(data)
    followersJson = json.loads(data.decode())
    followersJson = followersJson.get('msg')[1]
    followersInfo += followersJson

    if offset == followersCountInt:
        break
print('获取关注者完成')

#答案关注人员地址
pUrlList = getFollowersPeopleUrl(followersInfo)
voteWoman = 0
voteMan = 0
print('正在统计')
for pUrlElement in pUrlList:
    url = 'http://www.zhihu.com' + pUrlElement
    op = opener.open(url)
    data = op.read()
    data = ungzip(data)
    manFlag = getGender(data.decode())
    if manFlag == 0:
        voteWoman += 1
    else:
        voteMan += 1

print('关注总数 : ' + followersCountStr)
print('匿名用户 : ' + str(int(followersCountStr) - voteWoman - voteMan))
print('姑娘 : ' + str(voteWoman))
print('男的 : ' + str(voteMan))
