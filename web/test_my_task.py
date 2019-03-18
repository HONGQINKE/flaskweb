import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


from common import Commone,BasePage

import logging
import os


# 定义浏览器及初始化信息
dr = webdriver.Chrome()
commone = Commone()
basePage = BasePage(dr)

#初始化数据
id_number = commone.get_config_values('info', 'id_number')



#保存运行日志
commone.log()
basePage.login()

#点击Reviw
basePage.sleep(5)
basePage.click(['css','#app > div > div.ant-layout-sider.ant-layout-sider-dark.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span'])
basePage.sleep(5)


#点击My Task
basePage.click(['xpath','//*[@id="103$Menu"]/li[3]/a'])
time.sleep(5)
#输入身份证号码
basePage.type(['id','idNum'],id_number)
time.sleep(5)
#点击查询
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
#点击申请记录详情
time.sleep(5)
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(1) > a'])
#反欺诈框输入结果
basePage.type(['id','antiFraudResutl'],'ok')
#滚动下拉到底部
basePage.scoll('1000')
time.sleep(3)

#反欺诈结果点击Save
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.scrollForm > form > div.align-center > button.ant-btn.mtPercent.ant-btn-primary'])
#反欺诈点击Information Asset
time.sleep(3)
'''
#点击Clear
basePage.click(['xpath','//*[@id="idPhotoFit"]/label[1]/span[2]'])
#点击Yes
basePage.click(['css','#personPhotoFit > label:nth-child(1) > span:nth-child(2)'])
#点击Pass
basePage.click(['css','#kptCheckOnline > label:nth-child(1) > span:nth-child(2)'])
#输入Region信息
basePage.type(['id','religion'],'regionA')
#输入婚姻状态
basePage.click(['css','#maritalStatus > div > div > div'])
WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath('/html/body/div[4]').is_displayed())
menu =dr.find_element_by_xpath('/html/body/div[4]').find_element_by_xpath("/html/body/div[4]//ul/li[2]")
menu.click()
#滚动下拉到底部
js = "var q=document.documentElement.scrollTop=1000"
dr.execute_script(js)
#选择身份证省市区
basePage.click(['id','idProvince'])
WebDriverWait(dr, 30).until(lambda x: x.find_element_by_xpath('/html/body/div[5]').is_displayed())
menu =dr.find_element_by_xpath('/html/body/div[5]').find_element_by_xpath("/html/body/div[5]//ul[1]/li[1]")
menu.click()
menu = dr.find_element_by_xpath("/html/body/div[5]//ul[2]/li[1]")
menu.click()
menu = dr.find_element_by_xpath("/html/body/div[5]//ul[3]/li[1]")
menu.click()
#输入身份证详细地址
basePage.type(['id','idAddress'],'Address Detail')
'''
#提交保存
js = "var q=document.documentElement.scrollTop=1000"
dr.execute_script(js)
basePage.submit(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.loanMeterial > form > div > div > div.ant-col-13 > div.align-center > button.ant-btn.mtPercent.ant-btn-primary > span'])

#点击phone Check
#basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab > span'])
#下拉到底部
basePage.scoll('10000')
#点击Normal
basePage.click(['css','#checkSelf > label:nth-child(2) > span:nth-child(2)'])
#点击Normal
basePage.click(['css','#checkContact > label:nth-child(3) > span:nth-child(2)'])
#点击Normal
basePage.click(['css','#checkWork > label:nth-child(3) > span:nth-child(2)'])
#点击Approve
basePage.click(['css','<span>Approved</span>'])
#关闭浏览器
basePage.quit()

