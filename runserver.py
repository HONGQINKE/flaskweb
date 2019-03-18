import time
from selenium import webdriver


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

#点击Task Allocation
basePage.click(['xpath','//*[@id="103$Menu"]/li[4]/a'])
#输入身份证号码
basePage.type(['id','idNum'],id_number)

#点击查询
time.sleep(5)
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > form > div:nth-child(2) > div > button.ant-btn.ant-btn-primary'])
#点击任务分配
time.sleep(5)
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-table-wrapper.tableGrid > div > div > div > div > div > table > tbody > tr > td:nth-child(13) > button'])
#输入刘虹
time.sleep(5)
basePage.type(['id','name'],'liuhong')
#查询刘虹
basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div > div.ant-col-6 > button'])
#选择刘虹
time.sleep(5)
basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > label > span > input'])
#点击ok
basePage.click(['css','body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'])
#确认ok
time.sleep(3)
basePage.click(['css','body div.ant-modal-confirm .ant-modal-body button.ant-btn.ant-btn-primary'])
time.sleep(3)


#击My Task

basePage.click(['xpath','//*[@id="103$Menu"]/li[3]/a'])
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
#js="var q=document.documentElement.scrollTop=100000"
#basePage.execute_script(js)
basePage.scoll('10000')
time.sleep(3)
#反欺诈结果点击Save
basePage.click(['css','#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.scrollForm > form > div.align-center > button.ant-btn.mtPercent.ant-btn-primary'])
#反欺诈点击Information Asset
#driver.click('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab').click()
#点击Yes
time.sleep(3)
#driver.find_element_by_css_selector('.label.ant-radio-button-wrapper.ant-radio-button-wrapper-checked  .span.ant-radio-button.ant-radio-button-checked').click()
basePage.click(['xpath','//*[@id="idPhotoFit"]/label[1]/span[2]'])
basePage.click(['css','#personPhotoFit > label:nth-child(1) > span:nth-child(2)'])
basePage.click(['css','#kptCheckOnline > label:nth-child(1) > span:nth-child(2)'])
basePage.type(['id','religion'],'regionA')
#输入婚姻状态
#time.sleep(5)
#basePage.click(['css','#maritalStatus > div > div > div'])
#time.sleep(10)


basePage.button_drop()


#basePage.click(['css','a#d35c0a3c-1d22-4f12-fc5b-5c9348db6408 > ul > li:nth-child(2)'])
#ul = driver.find_element_by_css_selector('body div.ant-select-dropdown.ant-select-dropdown--single.ant-select-dropdown-placement-bottomLeft.ant-select-dropdown-hidden >div > ul >li:nth-child(2)')
#ul.find_element_by_css_selector(' li:nth-child(2)').click()
#选择居住地址
#滚动下拉到底部
#js="var q=document.documentElement.scrollTop=100000"
#basePage.execute_script(js)
basePage.scoll('1000')
time.sleep(3)
#输入居住详细地址
basePage.find_element_by_id('idAddress').send_keys('Address')
#点击保存
#点击Phone Check
basePage.find_element_by_css_selector('#app > div > div.ant-layout > div.mainContent.ant-layout-content > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab > span').click()
#关闭浏览器
basePage.quit()

