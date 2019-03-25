import os
import time
from appium import webdriver
from common import Mysql
import logging
from common import Commone

commone = Commone()
commone.log()
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
#华硕手机
#desired_caps['deviceName'] = 'HBAXJR00K412NC9'
#小米手机、
desired_caps['deviceName'] = 'albf48c'
desired_caps['app'] = PATH('E:\package\dev-sit.20190129121419.apk')
desired_caps['appWaitActivity'] = 'com.kpt.android.activity.StartActivity'
#desired_caps['appPackage'] = 'com.kpt.andriod'
#desired_caps['appActivity'] = 'com.kpt.android/.activity.StartActivity'
#desired_caps['appActivity'] = 'com.kpt.android/.activity.LeaderActivity '
# 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(t):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(t):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,t)




#启动App
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#模拟左滑动
swipLeft(1000)
swipLeft(1000)
#点击Mulai Coba
driver.find_element_by_id('com.kpt.android:id/startTxt').click()
time.sleep(5)
#确认允许手机定位
driver.find_element_by_id('android:id/button1').click()
#确认允许录制照片和视频
driver.find_element_by_id('android:id/button1').click()
#确认获取手机号码，IMEI,IMSI权限
driver.find_element_by_id('android:id/button1').click()
#输入手机号
driver.find_element_by_id('com.kpt.android:id/phoneEdit').send_keys('9999990001')
#点击登录
driver.find_element_by_id('com.kpt.android:id/loginBtn').click()
#连接数据库获取数据库中验证码
mysql = Mysql()
sql = "select CODE from pub_verification_code where phone =9999990001 order by CREATE_TIME desc LIMIT 0,1"
# 数据库查询结果，结果类型为Tuple
data = mysql.fetchone(sql)
# 提取元组中的验证码值
code = data[0][0]
logging.info('verification code is %s' % code)
#拆分Str类型的code为单个字符
code_list = list(code)
print(code_list)

#输入验证码
time.sleep(5)
#xf = driver.find_elements_by_class_name('android.widget.EditText')
driver.switch_to.frame(0)
driver.find_element_by_id('com.kpt.android:id/code1Edit').send_keys(code_list[0])
driver.find_element_by_id('com.kpt.android:id/code2Edit').send_keys(code_list[1])
driver.find_element_by_id('com.kpt.android:id/code3Edit').send_keys(code_list[2])
driver.find_element_by_id('com.kpt.android:id/code4Edit').send_keys(code_list[3])

#退出
driver.quit()


