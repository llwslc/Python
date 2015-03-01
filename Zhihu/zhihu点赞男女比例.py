import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import sys

#python 3.4.2
#需要在常用电脑上登录,不然会有验证码的问题

#不是男的则统计为姑娘
#匿名用户单独列出

#邮箱和密码
email = 'xx@gmail.com'
password = 'xx'
#答案链接地址
answerurl = 'http://www.zhihu.com/question/26431968/answer/32770482'

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
url = answerurl
op = opener.open(url)
data = op.read()
data = ungzip(data)

#答案链接地址
data = data.decode()
voteCount = getVoteCount(data)
ansId = getAnswerId(data)
#http://www.zhihu.com/node/AnswerFullVoteInfoV2?params={"answer_id":"8449741"}
url = 'http://www.zhihu.com/node/AnswerFullVoteInfoV2?params={"answer_id":"' + ansId + '"}'

#答案点赞人员地址
#url = 'http://www.zhihu.com/node/MemberProfileCardV2?params={"url_token":"wu-ruo-xu"}'
op = opener.open(url)
data = op.read()
data = ungzip(data)
pUrlList = getPeopleUrl(data.decode())
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

print('点赞总数 : ' + voteCount)
print('匿名用户 : ' + str(int(voteCount) - voteWoman - voteMan))
print('姑娘 : ' + str(voteWoman))
print('男的 : ' + str(voteMan))
