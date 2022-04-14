import requests, os, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.touch_actions import TouchActions
from bs4 import BeautifulSoup
import time
from PIL import Image
from pathlib import Path
mobile_emulation = {
    'deviceName': 'Apple iPhone 4',
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},  # 定义设备高宽，像素比
    "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "  # 通过UA来模拟
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36 Edg/98.0.1108.50"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Edge("E:/msedgedriver.exe")

def getCode() -> str:
    img = driver.find_element_by_id("img_valiCode")
    img.screenshot("code.png")
    code = str(input())
    return code

def login() -> None:
    driver.get("http://yktfw.csust.edu.cn/Phone/Login")
    driver.find_element_by_id("txt_sno").send_keys("202002140917")
    driver.find_element_by_id("txt_pwd").send_keys("021025")
    driver.find_element_by_id("txt_yzm").send_keys(getCode())
    driver.find_element_by_id("btn_login").click()
    time.sleep(20)
    driver.get("http://yktfw.csust.edu.cn/PPage/ComePage")
'''
def getCookie() -> None:
    cookie = driver.get_cookies()
    Path('cookie.txt').write_text(json.dumps(cookie))
'''



login()