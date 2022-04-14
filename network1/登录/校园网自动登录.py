# 导入包
import time,socket,requests,random
# 判断网络状态
def is_net_ok():
    s=socket.socket()
    s.settimeout(0.3)
    try:
        status = s.connect_ex(('www.baidu.com',443))
        if status == 0:
            s.close()
            return True
        else:
            s.close()
            return False
    except:
        s.close()
        pass    # 没网就继续下一步，什么都不用管


#获取IPv4地址
def getIP():
    hostname = socket.gethostname()
    ip =socket.gethostbyname(hostname)
    return ip


# 登录
def login_request():
    LOGIN_PAGE_URL = "http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanuserip={0:}&wlanacip=192.168.130.254&wlanacname=ME60-X8-1&mac=c9-cc-a2-09-15-de&ip={0:}&enAdvert=0&queryACIP=0&loginMethod=1".format(getIP())
    n = random.randint(0, len(ACCS))
    Username = str(ACCS[n])
    data1 = {"DDDDD": ",0," + Username,"upass": "123456","OMKKey": "123456","R1": "0","R2": "0","R3": "0", "R6": "0","para": "00"}
    try:
        result = requests.post(LOGIN_PAGE_URL, data = data1)
        print (result.text)
        if is_net_ok():
            return True
        else :
            return False
    except:
        return False



# 主程序
def main():
    if is_net_ok():    # 有网
        return True
    else:   #没网
        if login_request():   # 登录成功
            return True
        else:
            return False


try:
    f = open("Accounts.txt","r")   # 设置文件对象
    ACCS = f.read().splitlines()
    f.close() # 关闭文件
except Exception as e:
    print(e)
    q = input()
while True:
    try:
        if main():
            time.sleep(1)
    except Exception as e:
        print(e)
        q = input()